Title: hastebin – Pastebin Server und Client
Date: 28.08.2013, 17:46
Tags: [planet, Node.js]

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

---

Ein kleiner Nachtrag zum 15. November '13: nach ein paar Wochen fiel mir auf,
dass das Gem recht krepelig ist und es auch einfacher mit `curl` geht:

```sh
function haste
    printf "https://paste.posativ.org/"
    curl -s -X POST https://paste.posativ.org/documents --data-binary "@-" \
    | cut -d ":" -f 2 | grep -oE '"\w+"' | tr -d '"' 
end
```

Außerdem möchte man sowohl Google Analytics als auch jQuery auf Googles CDN aus dem Template entfernen:

```diff
diff --git a/static/index.html b/static/index.html
index fb93642..78cc1de 100644
--- a/static/index.html
+++ b/static/index.html
@@ -7,7 +7,7 @@
   <link rel="stylesheet" type="text/css" href="solarized_dark.css"/>
   <link rel="stylesheet" type="text/css" href="application.css"/>
 
-  <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
+  <script type="text/javascript" src="jquery.min.js"></script>
   <script type="text/javascript" src="highlight.min.js"></script>
   <script type="text/javascript" src="application.min.js"></script>
 
@@ -62,18 +62,6 @@
   <div id="linenos"></div>
   <pre id="box" style="display:none;" tabindex="0"><code></code></pre>
   <textarea spellcheck="false" style="display:none;"></textarea>
-
-  <script type="text/javascript">
-          var _gaq = _gaq || [];
-          _gaq.push(['_setAccount', 'UA-27329119-1']);
-          _gaq.push(['_trackPageview']);
-          (function() {
-                  var ga = document.createElement('script'); ga.type = 'text/javascript';
-                  ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'htt
-                  var s = document.getElementsByTagName('script')[0]; s.parentNode.insert
-          })();
-  </script>
```

[1]: https://github.com/posativ/paste.posativ.org
[2]: https://github.com/seejohnrun/haste-server
[3]: http://softwaremaniacs.org/soft/highlight/en/
