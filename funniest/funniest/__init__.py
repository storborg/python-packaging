## This document is licensed under `CC-BY-SA <http://creativecommons.org/licenses/by-sa/3.0/>`
## (C) 2013, Scott Torberg

from markdown import markdown

def joke():
    return markdown(u'Wenn ist das Nunst\u00fcck git und Slotermeyer?'
                    u'Ja! ... **Beiherhund** das Oder die Flipperwaldt '
                    u'gersput.')
