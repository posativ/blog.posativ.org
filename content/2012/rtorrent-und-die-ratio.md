Title: rTorrent und die Ratio
Date: 04.11.2012, 23:58
Tags: [rtorrent, Open Source]

Bevor ich's vergesse: [rTorrent][1] ist der beste Torrent-Client  für jedes
gescheite Betriebssystem. Wobei sich für den schnellen Torrent für zwischendurch
[aria2][2] auch gut eignet. Leider wird letzteres häufig bei geschlossenen 
Urlaubsfotosaustausch-Trackern häufig gesperrt – und der User-Agent lässt sich
leider nicht via `--useragent=foo/1.0` ändern.

Urlaubsfotos (sic!) austauschen kennt ihr ja, das Problem ist allerdings, dass
man auch selbst viele Urlaubsfotos hochladen muss, sonst fliegt man. Leider
haben die meisten keinen dicken Upstream, was das ganze im im Vergleich zu
locker 7 MB/sec in Schweden schwierig macht. Hier kommt `rtorrent`, genauer
gesagt `libtorrent` ins Spiel. [libtorrent][3] ist open-source und der Grund,
warum `rtorrent` sogar auf meinem lahmen SheevaPlug Spaß machte. Aber zurück zu
dem Problem mit der Ratio: nicht etwa der Tracker prüft, was man herunter- und
hochlädt – nein, das ist die Aufgabe des Clients. Hrhr.

    :::diff
    diff --git a/src/tracker/tracker_http.cc b/src/tracker/tracker_http.cc
    index c3436d4..5447d68 100644
    --- a/src/tracker/tracker_http.cc
    +++ b/src/tracker/tracker_http.cc
    @@ -160,7 +160,7 @@ TrackerHttp::send_state(int state) {
       uint64_t completed_adjusted = info->completed_adjusted();
       uint64_t download_left = info->slot_left()();

    -  s << "&uploaded=" << uploaded_adjusted
    +  s << "&uploaded=" << (16*uploaded_adjusted)
         << "&downloaded=" << completed_adjusted
         << "&left=" << download_left;

Das ist der entscheidende Punkt in der `libtorrent`. Ich selbst habe noch nie 
probiert, die Download-Größe zu fälschen. Das fällt eventuell auf, wenn jemand
zwar fünfzig Bilder heruntergeladen, aber jeweils nur 140 MiB statt 1,4 GiB. Für
[homebrew][4]-Nutzer habe ich hier auch gleich die passende [Formula][5]. Ich
liebe freie Software!

[1]: http://libtorrent.rakshasa.no/
[2]: http://aria2.sourceforge.net/
[3]: http://www.rasterbar.com/products/libtorrent/
[4]: http://mxcl.github.com/homebrew/
[5]: https://gist.github.com/4014160
