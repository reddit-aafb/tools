# Flair stats

| Flair | Count |
|:------|------:|
{% for (group, abbr, flair_class, flair_text, emoji), substats in stats.items() -%}
| [{{ flair_text }}](/r/{{ abbr|team_sr }}) | {{ substats._total }} |
{% endfor %}

## Dual flair breakdown

| Primary | Secondary | Count |
|:--------|:----------|------:|
{% for (group, abbr, flair_class, flair_text, emoji), substats in stats.items() -%}
| [{{ flair_text }}](/r/{{ abbr|team_sr }}) | | {{ substats._total }} |
{% for team, count in substats.items() -%}
{% if team != '_total' -%}
{% set (group, abbr, flair_class, flair_text, emoji) = team -%}
| | {{ group|upper }} {{ flair_text }} | {{ count }} |
{% endif -%}
{% endfor -%}
{% endfor -%}
