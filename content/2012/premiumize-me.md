Title: premiumize.me
Date: 2012-11-24 23:11
Tag: Python

Wem Torrents nicht behagen und sich auch mit 1 MB/s zufrieden gibt, kann ich den
titulierten Anbieter empfehlen. Das Problem kennt ihr ja sicherlich auch:
jegliche Urlaubsfotos werden auf irgendwelche obskuren Sharehoster wie
[rapidshare.com](https://rapidshare.com/), ~~Herrn Schmitz'
[Megaupload.com](http://www.megaupload.com/)~~ oder
[uploaded.to](http://uploaded.to/) hochgeladen. Kennt ihr ja. Um ohne Wartezeit,
Bandbreitenbeschränkung und Trafficlimits Urlaubsfotos herunterzuladen, bedarf
es relativ kostspieligen Premium-Accounts zwischen fünf und zehn Euro je Monat.

Da die Urlaubsfotos zudem meist auf verschiedene Anbieter hochgeladen werden,
benötigt man schon drei oder mehr Accounts bei solchen dubiosen Anbietern. Da
kommt [Premiumize Me][1] ins Spiel: einmal Zahlen, bei fast™ allen Hostern mit
mäßiger – um die 1 MB/s – Geschwindigkeit herunterladen. Laut ihren AGBs darf
man sich keine Accounts teilen, aber das ist Quatsch. Selbst als ich von
Alice auf Tele Columbus gewechselt habe (vorher hatten wir beide Alice), haben
die das nicht gemerkt. Naja, deren System ist ja auch in PHP geschrieben.

Gibt auch andere wie [zevera.com]() und [real-debrid.com]() – letzteres hat
praktisch immer "Wartungsarbeiten" bei populären Hostern und ersteres ein
ziemlich behindertes Webinterface und genauso lange Wartezeiten wie die
eigentlichen Hoster. Active Server Pages halt. Alle drei bieten aber (unter
anderem) [paysafecard](http://www.paysafecard.com/de/de-paysafecard/) an ;-)

Weshalb ich das Thema hier eigentlich bringe: [Premiumize Me][1] hat eine REST
API und eignet sich damit hervorragend für `aria2c -i links -j 16`. Auch wenn
die einzelnen Streams nicht so schnell sind, 16 parallel lasten auch meine
Leitung aus.

[1]: https://secure.premiumize.me/

Ich habe mir ein kleines Skript für Python geschrieben, das in
`/usr/local/bin/premiumize` residiert. Als Apple-Hipster mache ich dann einfach
`pbpaste | premiumize > links` und werfe [aria2](http://aria2.sourceforge.net/)
an. Manchmal auch in Kombination mit [/decrypt/](https://posativ.org/decrypt/).

    :::python
    #!/usr/bin/env python

    import sys
    import os
    import io
    import json
    import requests  # easy_install requests

    from urllib import urlencode
    from time import strftime, gmtime


    def build(url, query):
        return url.rstrip('/') + '?' + urlencode(query)


    def info(url, user, passwd):
    
        query = {'method': 'accountstatus', "params[login]": user,
                 "params[pass]": passwd}

        r = requests.get(build(url, query))
        try:
            data = json.loads(r.content)["result"]
        except ValueError:
            raise
        except KeyError:
            print "Invalid credentials"
            sys.exit(1)
    
        print "%s (%s)" % (data['account_name'], data['type'])
        print "expires at %s" % strftime('%d. %b %Y', gmtime(data['expires']))
        print "traffic left: %0.2f GB" % data.get('trafficleft_gigabytes', 0.0)


    def download(url, user, passwd, link):
    
        query = {'method': 'directdownloadlink', 'params[login]': user,
                 'params[pass]': passwd, 'params[link]': link}
        data = json.loads(requests.get(build(url, query)).content)
        
        if data.get('result', None) is None:
            print >> sys.stderr, data['status'], data['statusmessage']
            sys.exit(1)
    
        return data['result']['location']


    if __name__ == '__main__':
    
        url = 'https://api.premiumize.me/pm-api/v1.php'
        user = 'UR USERNAME'
        passwd = 'UR PASSWORD'
    
        if len(sys.argv) <= 1:
            info(url, user, passwd)
            sys.exit(0)
    
        if os.path.isfile(sys.argv[1]):
            with io.open(sys.argv[1]) as fp:
                links = [line.strip() for line in fp if line.strip()]
        else:
            links = sys.argv[1:]
    
        for link in links:
            print >> sys.stderr, link
            print download(url, user, passwd, link)

        sys.exit(0)


Für 2.6 ≥ python > 3.0 + [requests](http://docs.python-requests.org/en/latest/).
    

