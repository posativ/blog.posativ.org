# -*- encoding: utf-8 -*-
# This is your config file.  Please write in a valid python syntax!
# See http://acrylamid.readthedocs.org/en/latest/conf.py.html

from os.path import join, dirname, basename

SITENAME = "mecker. mecker. mecker."
WWW_ROOT = "http://blog.posativ.org/"
THEME = "theme/"

AUTHOR, NICK = "Martin Zimmermann", "posativ"
EMAIL = "info@posativ.org"

METASTYLE = 'native'

THEME_IGNORE = ['*.swp']
CONTENT_IGNORE = ["drafts/*", "bak/*"]
CONTENT_EXTENSION = '.md'
STATIC = ["assets/"]
STATIC_IGNORE += ['.DS_Store']
STATIC_FILTER += ['SASS']

md = '+'.join(['Markdown',
     'codehilite(css_class=highlight)', 'attr_list', 'fenced_code',
     'mathml', 'sup', 'sub', 'delins', 'footnotes', 'abbr'])

FILTERS = [md, 'typo', 'h1', 'acronyms']
FILTERS_DIR += ['filters/']

VIEWS = {
    "/": {
        "filters": ['sum', 'hyph'],
        "pagination": "/page/:num/",
        "view": "index",
        "items_per_page": 12
    },
    "/:year/:slug/": {
        "filters": "hyph", "views": ["entry"]#, "draft"]
    },
    "/drafts/:slug/": {'view': 'draft'},
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
       "view": "tag", "template": "tags.html", "items_per_page": 1000
    },

    # produce a full text version of all Linkschleudern
    "/linkschleuder/" : {
         "filters": "hyph", "view": "index", "items_per_page": 1000,
         "if": lambda e: 'Links' in e.tags
    },

    # atom feed for those
    "/linkschleuder/feed/" : {
         "filters": "h2", "view": "atom",
         "if": lambda e: 'Links' in e.tags
    },

    "/sitemap.xml": {"view": "sitemap"}
}

SUMMARIZE_LINK = '<span>&#8230;<a href="%s" class="continue">weiterlesen</a>.</span>'
TYPOGRAPHY_MODE = "a"

PERMALINK_FORMAT = "/:year/:slug/"
DATE_FORMAT = "%d.%m.%Y, %H:%M"
DISQUS_SHORTNAME = "posativ"

DEPLOYMENT = {
    "ls": "ls",
    "echo": "echo $OUTPUT_DIR",
    'default': 'rsync -av --delete --exclude=".git/" $OUTPUT_DIR www@morloch:blog.posativ.org',
}

ACRONYMS_FILE =  "acronyms.txt"

HOOKS_MT = False
HOOKS = {
    "shots/.+\.(jpe?g|png)": (
        'convert -thumbnail 150x150^ -gravity center -extent 150x150 %1 %2',
        lambda p: join(dirname(p), 'thumbs/', basename(p)))
}

