Title: hastebin – Pastebin Server und Client
Date: 28.08.2013, 17:46
Tags: [Planet, Node.js]

Ein eigener Pastebin, warum nicht. Ich hatte meinen [selbst geschrieben][1],
allerdings nicht wirklich KISS zu deployen und ein Client-Skript erst recht
nicht. Jetzt nutze ich [Hastebin][2], ein Pastebin geschrieben in Node.js, und
einem Ruby (sic) Tool als CLI.

![Hastebin Screenshot](/img/2013/hastebin.png){:.center}

Die Installation ist recht simpel und viel tut die Anwendung auch nicht: Text
in einer Redis-Instanz speichern (in Datei oder memcached auch möglich) und
mit etwas [Highlight.js][3] bunt machen.  Als CLI noch `gem install haste`
installieren, `HASTE_SERVER=http://example.org` setzen und mit `cat datei.py |
haste` (useless use of cat) pastieren.

[1]: https://github.com/posativ/paste.posativ.org
[2]: https://github.com/seejohnrun/haste-server
[3]: http://softwaremaniacs.org/soft/highlight/en/
