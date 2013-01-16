Title: Linkschleuder #29
Date: 16.01.2013, 11:27
Tags: [Links, planet, JavaScript, UNIX]

Eine Linkschleuder hatten wir lange nicht mehr. Hab ungefähr über 9000 Links
über die Weihnachtsferien gesammelt und nun die BESTEN der BESTEN [^1] abgetippt:

- [Project Honey Pot](https://www.projecthoneypot.org/) – ziemlich
  zuverlässige Spam- und Harvestingerkennung, wenn man den Honigtopf eine Weile
  auf seiner Website (unsichtbar) verlinkt. Hatte massives Spamaufkommen bei
  [meinem Pastebin](http://paste.posativ.org/) und nach nur einer Woche hatte
  Project Honey Pot nahezu alle Spammer anhand der IP erkannt.
- [Regexper](http://www.regexper.com/) – ~~JavaScript~~ Perl-style regular
  expressions als Automat visualisieren.
- [jq](http://stedolan.github.com/jq/) – möchte das `awk`, `sed`, `grep` für
  JSON sein. Allerdings ist die Query-Syntax doch sehr gewöhnungsbedürftig.
- [PeerVPN](http://www.peervpn.net/) – auf dem Kongress kennengelernt, ist quasi
  ein ~~Bittorrent~~ Retroshare für VPNs für alle Betriebssysteme mit TUN/TAP
  Devices (also *nicht* OS X).
- [Darling](http://darling.dolezel.info/en/Darling) – nach Wine gibt es
  vielleicht auch demnächst einen Emulator von OS X. Yay.
- [SSHGuard](http://www.sshguard.net/) – normalerweise nutze ich
  [fail2ban](http://www.fail2ban.org/wiki/index.php/Main_Page) gegen
  Brute-Force-Angriffe gegen meine Dienste, aber SSHGuard unterstützt – anders
  als der Name vermuten lässt – auch Dienste neben SSH, ist allerdings in C
  geschrieben und hat eine hübschere Website.
- [git-extras](https://github.com/visionmedia/git-extras) – ein paar nützliche
  Utilities für [git](http://git-scm.com/) (via [cmur2](//mycrobase.de/)).
- [chktex](http://www.nongnu.org/chktex/) – ~~fsck~~ Lint für LaTeX, sicherlich
  nützlich für meine baldige Bachelor-Arbeit.
- [memusg](https://gist.github.com/526585) – kurz für *memory usage*, ist ein
  kleiner Wrapper, der alle (per default) 0.1 Sekunden nach dem RAM-Verbrauch
  guckt und hinterher den Peak ausgibt. Ziemlich praktisch (via [Stack
  Overflow](http://stackoverflow.com/q/774556)).
- [dcfldd](http://dcfldd.sourceforge.net/) – entweder `dcfldd` oder
  `dd if=/dev/ad0 | pv -s 512M | dd of=/dev/ad1`, je nachdem was
  leichter zu merken ist. Fairerweise kann `dcfldd` noch mehr unsinniges Zeug
  wie beispielsweise CRCen, Splitten oder Loggen.
- [Curse The Weather](http://opensource.hld.ca/trac.cgi/wiki/CurseTheWeather) –
  [zeigt das aktuelle Wetter](/img/2013/ctw.png) von weather.com sowie die
  Vorhersage für die nächsten fünf Tage an (leider nicht `easy_`zu`install`ieren).
- [Glances](http://nicolargo.github.com/glances/) – unterstützt im Gegensatz zu
  `htop` auch \*BSD (beide via [Inconsolation](https://inconsolation.wordpress.com/)).

[^1]: !1
