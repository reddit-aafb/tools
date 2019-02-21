# Just the {{ primary.text }}

[Click here](/message/compose?to=aafb_robot&subject={{ "Request flair /r/"|urlencode }}{{ sub.display_name }}&message=primary%3Aaaf-{{ abbr }})

# Dual Flair

## NFL

{% for teamabbr, team in secondary.nfl|dictsort -%}
* [{{ primary.text }} • {{ team.text }}](/message/compose?to=aafb_robot&subject={{ "Request flair /r/"|urlencode }}{{ sub.display_name }}&message=primary%3Aaaf-{{ abbr }}%20secondary%3Anfl-{{ teamabbr }})
{% endfor %}

## CFL

{% for teamabbr, team in secondary.cfl|dictsort -%}
* [{{ primary.text }} • {{ team.text }}](/message/compose?to=aafb_robot&subject={{ "Request flair /r/"|urlencode }}{{ sub.display_name }}&message=primary%3Aaaf-{{ abbr }}%20secondary%3Acfl-{{ teamabbr }})
{% endfor %}

## NCAA

Stay tuned...
