Title: Qualitätssoftware
Date: 07.02.2013, 21:58
Tags: [UNIX, planet]

Gerade ein [sehr amüsantes "Paper"][1] über -- nunja -- die Realität von
UNIX/Linux gelesen. Bei `libtool`

> At the bottom of the food chain, so to speak, is libtool, which tries to hide
> the fact that there is no standardized way to build a shared library in Unix.

und dessen `./configure`-Skript

> Today's Unix/Posix-like operating systems, even including IBM's z/OS
> mainframe version, as seen with 1980 eyes are identical; yet the 31,085 lines
> of configure for libtool still check if <sys/stat.h> and <stdlib.h> exist,
> even though the Unixen, which lacked them, had neither sufficient memory to
> execute libtool nor disks big enough for its 16-MB source code.

<!-- break -->

das gerade einmal 26 verschiedene Fortran Compiler sucht und jedes mal testet, ob
`-g` verfügbar ist, bleibt kein Auge trocken.

> This is probably also why libtool's configure probes no fewer than 26
> different names for the Fortran compiler my system does not have, and then
> spends another 26 tests to find out if each of these nonexistent Fortran
> compilers supports the -g option.

Das erinnert mich gleich wieder an die Installation von Node.js aus den
Quellen, welche erstmal ein aktuelles Python zur Konfiguration braucht.

[1]: https://queue.acm.org/detail.cfm?id=2349257
