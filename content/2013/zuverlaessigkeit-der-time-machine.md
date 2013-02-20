title: Um die Zuverlässigkeit zu verbessern, muss Time Machine ein neues Backup für Sie erstellen. ***
slug: zuverlaessigkeit-der-time-machine
date: 20.02.2013, 15:09
tags: [OS X, Rant]

**\* Dafür müssen wir Ihr altes Backup aufgrund technischer Inkompetenz löschen.
Das tut uns Leid.

![Fehlermeldung als Inkarnation eines Bildes](/img/2013/time-machine.png){:.center}

Meh.

# Not the State of Art

So sehr ich Time Machine auch mag -- system-integriert, halbwegs schnell, Booten
vom Backup -- so sehr hasse ich es auch. Das liegt viel weniger am `backupd`,
sondern an den technischen Unstimmigkeiten, die mir das Leben als Nerd schwer
machen:

  * keine Deduplikation (dafür hardlinks, doch dazu später mehr)
  * keine Prüfsummen, d.h. wenn sich durch das Wiederherstellen eines Backups
    die Zeitstempel oder Permissions ändern, meint Apple, alles erneuert sichern
    zu müssen.
  * Backup geht nach einer bestimmten Zeit einfach "kaputt" (siehe Titel)
  * proprietäres, retardiertes Format: [Sparsebundle][1]

Wenn man im Hinterkopf hat, dass Apple zwar schön [`rsnapshot`][2]-mäßig
ungeänderte Revision per Hardlink ~~dedupliziert~~ referenziert, aber gerade
auf Dateisystemebene massive Probleme [^1] mit eben diesen Hardlinks hat, kann
ich nachvollziehen, warum Apple ein Backup lieber als "verloren" für weitere
Backups markiert, als Gefahr zu laufen, dass der Unterbau kaputt geht.

Das mag zwar den gemeinen Nutzer nicht treffen, aber mich traf es. Datenplatte
wegen Windows 7/8 Installation gewipedt und später meine Musiksammlung + paar
Filme (nur ~150GB) wiederhergestellt. Zack, just nach der Wiederherstellung
fängt OS X nun an, diese "neuen" Dateien vollständig zu sichern. Zwei Tage
später war das Backup nun nicht mehr "zuverlässig". Gratulation, Apple.

[1]: https://en.wikipedia.org/wiki/Sparse_bundle#Sparse_bundle
[2]: http://www.rsnapshot.org/

[^1]: [Ars Technica über die Probleme mit HFS+ Hardlinks.
      ](http://arstechnica.com/apple/2011/07/mac-os-x-10-7/12/#hfs-problems)
      Angesichts dieser Software-Architektur würde es mich nicht verwundern,
      wenn dieses Problem auch in den Sparsebundles existiert.

# ZFS

Mein Time-Machine Backend ist ZFS+netatalk -- in der absurden Hoffnung, Apple
würde unverschlüsselte Backups als simple Dateien ablegen, sodass ZFS'
Deduplikation greift. Ha, Pustekuchen! Nachdem ich mein altes Backup (~350 GB,
nur zwei Monate alt) aufgeben musste, gibt ZFS den Speicherplatz wohl wegen der
vielen Dateien nicht mehr frei [^2]. Yay.

```sh
$ du -sh /data/backup/
552G    /data/backup/
$ zfs list /data/backup/
NAME          USED  AVAIL  REFER  MOUNTPOINT
data/backup   848G   176G   848G  /data/backup
```

Weiter geht's dann wohl mit einem Kommentar von "[Time Machine sucks, use rsync
instead][3]" `tym`, [Time rsYnc Machine][4]. Aber der Weisheit letzter Schluss
ist das auch nicht: Booten vom Backup geht, komplette Wiederherstellung ebenfalls
nicht. Statt `fsevent` wird jedes mal das komplette Dateisystem auf Änderungen
überprüft. Schön ist anders.

[3]: http://brian.windheim.org/2012/time-machine-sucks-use-rsync-instead
[4]: http://dragoman.org/tym/

[^2]: siehe [gmane.os.solaris.zfs/35935
            ](http://comments.gmane.org/gmane.os.solaris.opensolaris.zfs/35935)

