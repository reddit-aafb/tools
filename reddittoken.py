#!/usr/bin/env python
# Copyright 2016 Bryce Boe
# Copyright 2018 Jonas Häggqvist

"""This example demonstrates the flow for retrieving a refresh token.

In order for this example to work your application's redirect URI must be set
to http://localhost:8080.

This tool can be used to conveniently create refresh tokens for later use with
your web application OAuth2 credentials.

"""
import praw
import random
import socket
import sys
from urllib.parse import urlparse

ALL_SCOPES = ['creddits', 'edit', 'flair', 'history', 'identity',
                  'modconfig', 'modcontributors', 'modflair', 'modlog',
                  'modothers', 'modposts', 'modself', 'modwiki',
                  'mysubreddits', 'privatemessages', 'read', 'report',
                  'save', 'submit', 'subscribe', 'vote', 'wikiedit',
                  'wikiread']

def receive_connection(bindhost='0.0.0.0', listenport=8080):
    """Wait for and then return a connected socket..

    Opens a TCP connection on port 8080, and waits for a single client.

    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((bindhost, listenport))
    server.listen(1)
    client = server.accept()[0]
    server.close()
    return client


def send_message(client, message):
    """Send message to client and close the connection."""
    client.send('HTTP/1.1 200 OK\r\n\r\n{}'.format(message).encode('utf-8'))
    client.close()

def obtain(reddit, scopes, implicit = False):
    if 'all' in scopes:
        scopes = ALL_SCOPES
    state = str(random.randint(0, 65000))
    url = reddit.auth.url(scopes, state, 'permanent', implicit = implicit)
    print('Now open this url in your browser: '+url)
    sys.stdout.flush()

    redirect_uri_port = urlparse(reddit.config.redirect_uri).port
    client = receive_connection(listenport=redirect_uri_port)
    data = client.recv(1024).decode('utf-8')
    param_tokens = data.split(' ', 2)[1].split('?', 1)[1].split('&')
    params = {key: value for (key, value) in [token.split('=')
                                              for token in param_tokens]}

    if state != params['state']:
        msg = 'State mismatch. Expected: {} Received: {}'.format(state, params['state'])
        send_message(client, msg)
        raise Exception(msg)
    elif 'error' in params:
        send_message(client, params['error'])
        raise Exception(params['error'])

    refresh_token = reddit.auth.authorize(params['code'])
    send_message(client, 'refresh_token = {}'.format(refresh_token))
    return refresh_token

def ensure_scopes(reddit, scopes = None, implicit = False):
    if scopes is None and 'scopes' in reddit.config.custom:
        scopes = list(map(lambda s: s.strip().lower(), reddit.config.custom['scopes'].split(',')))

    if 'all' in scopes:
        scopes = ALL_SCOPES

    if type(scopes) == str:
        scopes = list(map(lambda s: s.strip().lower(), scopes.split(',')))

    if reddit.read_only or not reddit.auth.scopes().issuperset(scopes):
        refresh_token = obtain(reddit, scopes, implicit = False)
        print("Insert the following into your praw.ini:\nrefresh_token = {}".format(refresh_token))
        sys.exit(1)

def main():
    """Provide the program's entry point when directly executed."""
    print('Go here while logged into the account you want to create a '
          'token for: https://www.reddit.com/prefs/apps/')
    print('Click the create an app button. Put something in the name '
          'field and select the script radio button.')
    print('Put http://localhost:8080 in the redirect uri field and '
          'click create app')
    client_id = input('Enter the client ID, it\'s the line just under '
                      'Personal use script at the top: ')
    client_secret = input('Enter the client secret, it\'s the line next '
                          'to secret: ')
    commaScopes = input('Now enter a comma separated list of scopes, or '
                        'all for all tokens: ')

    scopes = commaScopes.lower().strip().split(',')

    reddit = praw.Reddit(client_id=client_id.strip(),
                         client_secret=client_secret.strip(),
                         redirect_uri='http://localhost:8080',
                         user_agent='praw_refresh_token_example')
    try:
        obtain(reddit, scopes)
        return 0
    except Exception as e:
        print(e)
        return 1
