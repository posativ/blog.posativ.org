---
title: Services Update
date: 31.08.2012, 17:01
tags: [CloudApp, regenwolken, Git, Firefox, Sync]
---

Wer jetzt denkt, ich schreibe jetzt nur, um zwischen den Linkschleudern immer
ein paar reguläre Texte zu haben – der hat recht! Nichtsdestotrotz möchte ich
einige Sachen Projekte erwähnen, an denen ich derzeit wieder rumwerkle und auch
bei mir hoste:

- [rw.posativ.org](http://rw.posativ.org/) – regenwolken Instanz, voll
  funktionsfähig trotz `501 Not Implemented`
- [posativ.org/weave/](https://posativ.org/weave/) – Firefox Sync Server
- [posativ.org/git/](https://posativ.org/git/) – simple Git Viewer
- [posativ.org/decrypt/](http://posativ.org/decrypt/) – online RSDF, CCF und DLC
  encryption (keine Updates hierzu, wollt's nur erwähnen)

#  [regenwolken – an open source CloudApp server][0]

Vor knapp einem Jahr [hatte ich ihn schon angekündigt][1], damals™ noch in der
0.1-alpha Phase. Ein Jahr, ein Frameworkwechsel und vier Versionen später bin
ich inzwischen bei 0.5 stable (!1) angelangt.

Wer das noch nicht kennt: [CloudApp][2] ist ein praktisches Tool für OS X, mit
dem beispielsweise Screenshots sofort ohne Interaktion hochgeladen werden können
und die URL in die Zwischenablage kopiert wird. Der Service ist kostenlos und
auf 10 (oder 12?) Uploads pro Tag mit jeweils 25 MiB limitiert, mehr muss
bezahlt werden. Ist also kein DropBox-Klon, sondern einfach ein Service zum
schnell mal was teilen. Clients gibt es für jedes OS, speziell auch für die KDE
und Gnome 3 Oberfläche angepasst.

Regenwolken ist soweit ich weiß, *die* vollständigste Implementierung der
[CloudApp][2]-Serverseite. Naja, daneben gibt es auch nur einen proof of concept
in node.js namens [raincloud][3]. Mit Zusammenarbeit von [cmur2][4] gibt es
[demnächst auch grafische Clients][5], die ohne Editieren der Hosts-Datei
alternative Server nutzen können (derzeit nur mit der [cloudapp-cli][11]
möglich). Das hat den Vorteil, dass z.B. auch per HTTPS kommuniziert werden
kann, ohne ein Zertifikat für `my.cl.ly` ausstellen zu müssen.

Mal grob die Features von regenwolken:

- open source und *nicht* in PHP geschrieben
- inzwischen sehr [einfache Installation][6]
- komplette Implementierung von der CloudApp API
- echte private Items + HTTPS support (hat CloudApp weder noch)

Was allerdings fehlt, ist ein kleines Webinterface, da es z.B. für Android
keinen Clienten gibt. Ich hoffe, das bekomme ich auch noch hin.

# [weave-minimal – a Firefox Sync full-server fork][7]

Nächstes Projekt, meine alternative zum bloatigen Firefox Sync Server, ist
leider ~~broken by design~~ dysfunktional, da zwar der Sync funktioniert, aber
der Firefox später nicht mehr an die Daten kommt. Das Problem dabei ist jetzt,
dass weder meine Server-Implementierung noch Firefox das merkwürdig findet und
das Debugging sehr schwer wird, da alle Daten verschlüsselt sind.

Wie dem auch sei, bin ich jetzt dabei, die [Testsuite][8] für den Mozilla Sync
Server auf meinem Server anzuwenden. Allerdings ist das schwierig, weil die
Suite auf Standards scheißt und deren Server das sogar versteht, aber meiner
nicht. Bis dahin kann ich nur die funktionierende [PHP Implementierung][9]
\*duck\* ~~empfehlen~~ verlinken.

# [klaus – a simple Git web viewer that Just Works™][10]

Kam schonmal in der Linkschleuder vor, aber weil ich da unter anderem bei der
SmartHTTP Integration für Git geholfen habe und das Teil eh ganz cool finde,
nochmal verlinkt. Der Git (smart) HTTP Transport ist sogar bedeutend schneller als
via SSH (wenn vielleicht auch *nicht ganz* so sicher ;-).

[0]: https://github.com/posativ/regenwolken/
[1]: /2011/regenwolken-hosting-cloudapp-on-your-own-server/
[2]: http://developer.getcloudapp.com/
[3]: https://github.com/rixth/raincloud
[4]: http://mycrobase.de/
[5]: https://github.com/cmur2/jcloudapp/
[6]: https://github.com/posativ/regenwolken/#quickstart
[7]: https://github.com/posativ/weave-minimal
[8]: https://github.com/mozilla-services/server-full/tree/master/tests
[9]: https://www.ohnekontur.de/2012/06/24/fsyncms-version-0-11-setup-page/
[10]: https://github.com/jonashaag/klaus
[11]: https://github.com/cmur2/cloudapp-cli
