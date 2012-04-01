# -*- encoding: utf-8 -*-
# This is your config file.  Please write in a valid python syntax!
# See http://acrylamid.readthedocs.org/en/latest/conf.py.html

SITENAME = "mecker. mecker. mecker."
WWW_ROOT = "http://blog.posativ.org/"

AUTHOR = "posativ"
EMAIL = "info@posativ.org"
ENTRIES_IGNORE = ["drafts/*", "bak/*"]

FILTERS = ['markdown+codehilite(css_class=highlight)+mathml', 'typo', 'h1', 'acronyms']
VIEWS = {
    "/": {
        "filters": ['sum', 'hyph'],
        "pagination": "/page/:num",
        "view": "index",
        "items_per_page": 12
    },
    "/:year/:slug/": {
        "filters": "hyph", "view": "entry"
    },
    "/atom/index.xml": {
        "filters": "h2", "view": "atom"
    },
    "/rss/": {
        "filters": "h2", "view": "rss"
    },
    "/rss/planet/index.xml": {
        "filters": "h2", "view": "rss",
        "if": lambda e: "planet" in e.tags,
    },
    "/articles/": {
        "view": "articles"
    },
    "/atom/full/index.xml": {
        "filters": "h2", "view": "atom", "num_entries": 1000
    },
    "/tag/:name/": {
        "filters": ['sum', 'h1', 'hyph'], "view":"tag",
        "pagination": "/tag/:name/:num", "items_per_page": 12
    },
}

SUMMARIZE_IDENTIFIER = 'weiterlesen'

PERMALINK_FORMAT = "/:year/:slug/"
DATE_FORMAT = "%d.%m.%Y, %H:%M"
DISQUS_SHORTNAME = "posativ"
OUTPUT_IGNORE = ["js/", "files/", "img/", "images/", "*.css", "*.txt", "*.conf",
                 "google*", "style.sass", "favicon.ico"]
DEPLOYMENT = {
    "ls": "ls",
    "echo": "echo %s",
    'blog': 'rsync -av --delete %s www@morloch:~/blog.posativ.org/',
}

ACRONYMS_FILE =  "output/acronyms.txt"
