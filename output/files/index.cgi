#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cgi import FieldStorage
from mimetypes import guess_type
from os.path import join, basename
from os import walk

if __name__ == '__main__':

    req = FieldStorage().getvalue('p', None)
    inline = int(FieldStorage().getvalue('inline', '0'))

    if req and req != 'index.cgi':
        for root, dirs, files in walk('.'):
            for item in [join(root, file) for file in files]:
                if req == basename(item):
                    if inline:
                        if guess_type(item)[0].find('text/') >= 0:
                            print 'Content-Type: text/plain\n'
                            for line in open(item):
                                print line,
                        break
                    else:
                        print 'Content-Type: %s\n' % guess_type(item)[0]
                        for line in open(item):
                            print line,
                        break
    else:
        print 'Content-Type: text/plain\n'
        print '-- Wenn du das hier liest, so sei dir gewiss, dass es keine Fehlprogrammierung ist --\n'
        for root, dirs, files in walk('.'):
            print '   '*(len(root.rsplit('/'))-1) + '+' + root
            dirs.sort()
            if files or dirs: print '\n'.join('   '*len(root.rsplit('/')) + '|' + file for file in sorted(files))