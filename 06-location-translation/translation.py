import gettext

# Set the path to the translation files
gettext.bindtextdomain('translation', 'locale')
gettext.textdomain('translation')
_ = gettext.gettext

print(_('Hello, World!'))