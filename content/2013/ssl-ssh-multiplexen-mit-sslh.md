Title: sslh - ssl/ssh multiplexer
Date: 07.06.2013, 18:25
Filter: liquid
Tag: planet

Die meisten öffentlichen (Hotel-) WLANs haben alles außer Port 80 und 443
blockiert. Da hilft dann auch kein OpenVPN. [corkscrew][1] läuft nur
mit Apache und allgemein ist das Konzept doch eher fragwürdig. Wenn man SSH
doch nur auf Port 80/443 legen könnte... – kann man!

{% blockquote sslh http://www.rutschle.net/tech/sslh.shtml %}
sslh accepts connections on specified ports, and forwards them further based on tests performed on the first data packet sent by the remote client.
{% endblockquote %}

```sh
~> sslh -p 2a01:1e8:e16e:1337::1:443 -p 0.0.0.0:443 \
        --ssh localhost:22 --ssl localhost:4430
```

Fertig. Nginx noch anweisen, auf Port 4430 für SSL zu lauschen und schon
kann man sich mittels `ssh -p 443 user@server` verbinden und erhält über
ein <https://example.org/> weiterhin die Webseite. Neben SSH und SSL werden
auch noch XMPP (yay), OpenVPN und HTTP unterstützt -- und wenn das nicht
reicht, gehen auch noch reguläre Ausdrücke. Gefällt.

Einziger Nachteil ist leider, dass nginx nur noch `127.0.0.1` als IP-Adresse
sieht und `fail2ban` für den SSH-Server auf Port 443 [nicht out-of-the-box
funktioniert][2]; und dass es keine eingebaute Unterstützung für [Quassel][3]
gibt!1

– via [marmaro.de](http://marmaro.de/lue/txt/2013-05-24.txt)

[1]: http://www.agroman.net/corkscrew/
[2]: http://rutschle.net/pipermail/sslh/2012-January/000138.html
[3]: http://quassel-irc.org/
