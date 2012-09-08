# -*- encoding: utf-8 -*-
# This is your config file.  Please write in a valid python syntax!
# See http://acrylamid.readthedocs.org/en/latest/conf.py.html

SITENAME = "mecker. mecker. mecker."
WWW_ROOT = "http://blog.posativ.org/"
THEME = "theme/"

AUTHOR = "posativ"
EMAIL = "info@posativ.org"

CONTENT_IGNORE = ["drafts/*", "bak/*"]
STATIC = "dataset/"

FILTERS = ['markdown+codehilite(css_class=highlight)+mathml+sup+sub+delins', 'typo', 'h1', 'acronyms']
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
    "/atom/": {
        "filters": "h2", "view": "atom"
    },
    "/rss/": {
        "filters": "h2", "view": "rss"
    },
    "/rss/planet/": {
        "filters": "h2", "view": "rss",
        "if": lambda e: "planet" in e.tags,
    },
    "/articles/": {
        "view": "articles"
    },
    "/tag/:name/": {
        "filters": ['sum', 'hyph'], "view":"tag",
        "pagination": "/tag/:name/:num", "items_per_page": 12
    },

    # produce a full text version of all Linkschleudern
    "/linkschleuder/full/" : {
         "filters": "hyph", "view": "index", "items_per_page": 1000,
         "condition": lambda e: 'Links' in e.tags
    },

    "/sitemap.xml": {"view": "sitemap"},

    "/wiki/:slug/": {"view": "page", "condition": lambda e:
        e.filename.startswith("content/wiki/")},

#    "/wiki/changes/": {"view": "wikifeed", "condition": lambda e:
#        e.filename.startswith("content/wiki/")},
}

SUMMARIZE_LINK = '<span>&#8230;<a href="%s" class="continue">weiterlesen</a>.</span>'
TYPOGRAPHY_MODE = "a"

PERMALINK_FORMAT = "/:year/:slug/"
DATE_FORMAT = "%d.%m.%Y, %H:%M"
DISQUS_SHORTNAME = "posativ"
OUTPUT_IGNORE += ["/js/", "/files/", "/img/", "*.css", "*.txt",
                  "*.conf", "/google*", "*.sass", "favicon.ico"]
DEPLOYMENT = {
    "ls": "ls",
    "echo": "echo $OUTPUT_DIR",
    'blog': 'rsync -av --delete --exclude=".git/" $OUTPUT_DIR www@morloch:~/blog.posativ.org/',
}

ACRONYMS_FILE =  "acronyms.txt"
