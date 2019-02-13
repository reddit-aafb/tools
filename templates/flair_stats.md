# Flair stats

| Flair | Count |
|:------|------:|
{% for (sr, flair_class, flair_text), count in stats|dictsort(by='value', reverse=True) -%}
| [{{ flair_text }}](/r/{{ sr }}) | {{ count }} |
{% endfor -%}
