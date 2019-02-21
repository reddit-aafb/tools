# Select your AAF team below!

{% for abbr, teamflair in flair.aaf|dictsort(by='key') if abbr != 'AAF' -%}
* [Select the {{ teamflair.text }}](/r/{{ sub.display_name }}/wiki{{ page.name }}/{{ teamflair.text|lower }})
{% endfor -%}
* [Select the {{ flair.aaf.AAF.text }} Shield](/r/{{ sub.display_name }}/wiki{{ page.name }}/{{ flair.aaf.AAF.text|lower }})
