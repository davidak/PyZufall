Changelog
=========

Hier sind die Änderungen jeder Version dokumentiert.

Version 0.13.2
--------------

Veröffentlicht am 23.05.2016

- Unicode Fehler behoben, Kompatibilität mit Python 2/3 verbessert
- Python 3.2 wird nicht mehr unterstützt
- Viele Verbesserungen am Code und kleinere Fehler behoben

Version 0.13.1
--------------

Veröffentlicht am 08.07.2015

- Fehler bei Installation mit Python 3 behoben

Version 0.13
------------

Veröffentlicht am 14.03.2015

- Kompatibilität mit Python 2.7
- automatische Unittests mit `Travis-CI <https://travis-ci.org/davidak/PyZufall>`_ und `Test Coverage <https://coveralls.io/r/davidak/PyZufall?branch=master>`_
- :py:func:`pyzufall.generator.zeitpunkt` hinzugefügt
- :py:func:`pyzufall.generator.nickname` hinzugefügt
- :py:func:`pyzufall.generator.homepage` hinzugefügt
- :py:func:`pyzufall.helfer.uml` hinzugefügt
- :py:func:`pyzufall.generator.url` hinzugefügt
- :py:func:`pyzufall.generator.email` hinzugefügt
- veraltete Funktionen entfernt
- Dokumentation überarbeitet
- Viele Verbesserungen am Code und Fehler behoben

Version 0.12
------------

Veröffentlicht am 14.01.2014

- :py:func:`pyzufall.satz.satz_interessen` hinzugefügt
- :py:func:`pyzufall.helfer.aufzaehlung` ersetzt :py:func:`pyzufall.generator.interessen_liste`
- Keine Vergewaltigungen mehr. Das ist nicht witzig! Es braucht auch nicht über 20 Synonyme für Geschlechtsverkehr und Selbstbefriedigung. Durch diese Änderungen wird die Seriosität deutlich gesteigert!
- Dokumentation verbessert und aktualisiert
- Viele Verbesserungen am Code
- Viele kleine Fehler behoben

Version 0.11
------------

Veröffentlicht am 22.09.2013

- Funktion :py:func:`pyzufall.helfer.chance` hinzugefügt und :py:func:`pyzufall.helfer.e25` etc dadurch ersetzt
- Funktion :py:func:`pyzufall.generator.interessen_liste` hinzugefügt. Sie ersetzt :py:func:`pyzufall.generator.interesse`.
- Funktion :py:func:`pyzufall.helfer.str_add` mit Unittests hinzugefügt
- Ungleiche Elemente aus Listen werden jetzt mit der Funktion :py:func:`random.sample()` generiert.
- Doctests in Modulen hinzugefügt
- *Makefile* erstellt
- *setup.py* und *MANIFEST.in* hinzugefügt
- Dokumentation und README angepasst
- Seite :doc:`entwicklung` zur Dokumentation hinzugefügt
- Sphinx Parameter zu Docstrings hinzufügen
- viele kleine Fehlerbehebungen und Verbesserungen

Version 0.10.3
--------------

Veröffentlicht am 15.09.2013

- Dateien mit Datensätzen die Endung .txt gegeben, um deren Erweiterbarkeit hervorzuheben und spätere Bearbeitung zu vereinfachen
- LICENSE wieder ohne .rst, weil es nicht in `reStructuredText <http://de.wikipedia.org/wiki/ReStructuredText>`_ formatiert ist

Version 0.10.2
--------------

Veröffentlicht am 15.09.2013

- Changelog hinzugefügt und in Dokumentation eingebunden
- Dokumentation erweitert
- README und LICENSE auch mit `reStructuredText <http://de.wikipedia.org/wiki/ReStructuredText>`_ formatiert anstatt `Markdown <http://de.wikipedia.org/wiki/Markdown>`_, um einheitlich mit der Dokumentation zu sein

Version 0.10.1
--------------

Veröffentlicht am 13.09.2013

- Dokumentation an die neue Struktur angepasst
- Fehler in :py:func:`pyzufall.person._gen_interessen` behoben

Version 0.10
------------

Veröffentlicht am 13.09.2013

- Projekt umstrukturiert: **pyzufall** als Paket in mehrere Module aufgeteilt

Version 0.9
-----------

Veröffentlicht am 23.08.2013

- jedes Satz-Schema als Funktion
- Unittests mit nose hinzugefügt
- Modul person hinzugefügt
- README.md hinzugefügt
- LICENSE.md hinzugefügt mit GPLv3
- TODO-Seite in Dokumentation hinzugefügt, auf der Hinweise im Quelltext aufgelistet werden
- Entstehung zur Dokumentation hinzugefügt
- Struktur der Dokumentation angepasst
- viele kleine Änderungen

Version 0.8
-----------

Veröffentlicht am 23.07.2013

- Dokumentation mit Sphinx hinzugefügt
- Docstring für jede Funktion hinzugefügt

Vor der Version 0.8 gab es keine Versionsnummern, sie wurde als gefühlter Entwicklungsstand vergeben.

Alle Änderungen können den Kommentaren der `Commits im Repository <https://github.com/davidak/pyzufall/commits/>`_ entnommen werden.

Der erste Commit war am 27.08.2012.