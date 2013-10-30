Title: Isso – Ich schrei sonst
Date: 30.10.2013, 17:42
Tags: [planet, statische Seiten]

Da mein Blog aus statischen Seiten besteht, musste ich bisher [Disqus][1]
für Kommentare nutzen. Auch wenn ich Disqus keine bösen Hintergedanken
unterstelle -- immerhin [nutzen sie Python][2] --, wollte ich mich dieser
Abhängigkeit schon länger entziehen. Seit heute laufen daher die Kommentare
über eine Eigenentwicklung: [Isso][3] -- mit Livedemo!

<figure style="text-align: center;">
  <img src="/img/2013/duty_calls.png" alt="XKCD Duty Calls" width="300px" heigth="330px" />
  <figcaption>by Randall Munroe, CC BY-NC 2.5</figcaption>
</figure>

Keine Third-Party Server, ~~noch~~ kein Routing über die USA, halbwegs ansehnlich
und funktional. Wiederkehrende Nutzer können sich per E-Mail-Adresse das gleiche
Identicon wiederholen. Gespeichert wird in der Datenbank nur: [Hash][4] [^1] der
E-Mail-Adresse und /24 bzw. /48 der IP-Adresse für IPv4 respektive IPv6.

Administriert wird per E-Mail, Webinterface kann gerne kontributiert werden. Noch
sind die Kommentare unmoderiert, mal sehen, wie sich das Spamaufkommen entwickelt.

Der Quellcode steht unter [MIT][5] und ist auf [GitHub][6] zu finden.

[1]: https://disqus.com/
[2]: http://blog.disqus.com/post/62187806135/scaling-django-to-8-billion-page-views
[3]: http://posativ.org/isso/
[4]: https://en.wikipedia.org/wiki/PBKDF2
[5]: http://opensource.org/licenses/MIT
[6]: https://github.com/posativ/isso

[^1]: Leider nur 1000 Iterationen, weil JavaScript fucking langsam ist,
      empfohlen sind für das Jahr 2013 100.000 Iterationen.
