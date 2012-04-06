#!/usr/bin/env python
"""
# JavaScript
  - autocomplete title if possible
  - load urls + #1 meta #2 text
  - remove current HTML
  - find index in meta+text and return urls[index]
  - for entry in found
      + load given entry
      + highlight section
      + show full entry if clicked
      + show original content on close
"""

import re, json, os

from acrylamid.views import View
from collections import defaultdict


class SetEncoder(json.JSONEncoder):
   def default(self, obj):
      if isinstance(obj, set):
         return list(obj)
      return json.JSONEncoder.default(self, obj)


class Search(View):

    def generate(self, request):
        
        entrylist = [entry for entry in request['entrylist'] if not entry.draft]
        
        # table url -> id
        urls = {}
        # meta -> id
        meta = defaultdict(set)
        # word -> id
        words = defaultdict(set)
        
        for i, entry in enumerate(entrylist):
            urls[entry.permalink] = i
            
            meta[entry.author].add(i)
            for word in re.split(r"[.:,\s!?+=\(\)/-]+", entry.title):
                meta[word].add(i)
            for tag in entry.tags:
                meta[tag].add(i)
            
            for word in re.split(r"[.:,\s!?+=\(\)/-]+", entry.source):
                if len(word) < 3: continue
                words[word].add(i)
        
        urls = dict([(id, url) for url, id in urls.iteritems()])
        yield json.dumps({'urls': urls, 'meta': meta}, cls=SetEncoder), \
              os.path.join(self.conf['output_dir'], 'index.js')
        yield json.dumps(words, cls=SetEncoder), \
              os.path.join(self.conf['output_dir'], 'words.js')