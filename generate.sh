#!/bin/sh

if [ ! -f "aaf_schema.json" ]; then
    rm -f aaf_schema.py
    python3 -m sgqlc.introspection \
        --exclude-deprecated \
        --exclude-description \
        https://api.platform.aaf.com/v1/graphql \
        aaf_schema.json
fi

if [ ! -f "aaf_schema.py" ]; then
    sgqlc-codegen aaf_schema.json aaf_schema.py
fi
