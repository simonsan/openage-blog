#!/usr/bin/env python3

AUTHOR = "' OR 1=1; DROP TABLE blogposts; --"
SITENAME = 'openage dev updates'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = "theme/"

LINKS = (
    ('openage', 'http://openage.sft.mx/'),
    ('source code', 'https://github.com/SFTtech/openage/'),
    ('blog origin', 'https://github.com/SFTtech/openage-blog/'),
)

SOCIAL = ()

DEFAULT_PAGINATION = 5

RELATIVE_URLS = True

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
}

STATIC_PATHS = list(EXTRA_PATH_METADATA.keys())

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}