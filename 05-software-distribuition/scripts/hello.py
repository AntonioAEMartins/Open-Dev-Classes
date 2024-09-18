#!/usr/bin/env python3
import sys
import os
import locale
from babel.dates import format_date
from babel import Locale
import gettext
from datetime import datetime as Date

gettext.bindtextdomain('cli', 'locale')
gettext.textdomain('cli')
_ = gettext.gettext

language = os.getenv('LANGUAGE', 'en_US.UTF-8')
locale.setlocale(locale.LC_TIME, language)

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dev_aberto import hello

if __name__ == '__main__':
    date_string, name = hello()
    locale_code = language.split('.')[0].replace('-', '_')
    babel_locale = Locale.parse(locale_code)
    date = Date.strptime(date_string, '%Y-%m-%dT%H:%M:%SZ')
    formatted_date = format_date(date, locale=babel_locale)
    print(_('Último commit feito em:'), formatted_date, _(' por'), name)
