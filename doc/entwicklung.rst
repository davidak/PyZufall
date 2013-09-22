Entwicklung
===========

Bei der Entwicklung von **pyzufall** wird `git <http://git-scm.com/>`_ für die Versionierung eingesetzt.

Die Dokumentation wird mit `Sphinx <http://sphinx-doc.org/>`_ erzeugt und die Unittests durch `nose <http://nose.readthedocs.org/>`_ ausgeführt.

Repository runterladen
----------
::

	$ git clone https://github.com/davidak/pyzufall.git

.. note::

    Dafür muss `git <http://git-scm.com/>`_ installiert sein.

Unittests
---------

Um den Code auf deinem System zu testen, führe folgenden Befehl im heruntergeladenen Repository aus::

	imac:PyZufall davidak$ make test
	Doctest: pyzufall.generator.adjektiv ... ok
	Doctest: pyzufall.generator.band ... ok
	Doctest: pyzufall.generator.bandart ... ok
	Doctest: pyzufall.generator.baum ... ok
	Doctest: pyzufall.generator.beilage ... ok
	Doctest: pyzufall.generator.beruf_m ... ok
	Doctest: pyzufall.generator.beruf_w ... ok
	Doctest: pyzufall.generator.color ... ok
	Doctest: pyzufall.generator.datum ... ok
	Doctest: pyzufall.generator.essen ... ok
	Doctest: pyzufall.generator.farbe ... ok
	Doctest: pyzufall.generator.geburtsdatum ... ok
	Doctest: pyzufall.generator.gegenstand ... ok
	Doctest: pyzufall.generator.geschlecht ... ok
	Doctest: pyzufall.generator.interesse ... ok
	Doctest: pyzufall.generator.interessen_liste ... ok
	Doctest: pyzufall.generator.koerperteil ... ok
	Doctest: pyzufall.generator.nachname ... ok
	Doctest: pyzufall.generator.ort ... ok
	Doctest: pyzufall.generator.person_m ... ok
	Doctest: pyzufall.generator.person_objekt_m ... ok
	Doctest: pyzufall.generator.person_objekt_w ... ok
	Doctest: pyzufall.generator.person_w ... ok
	Doctest: pyzufall.generator.pflanze ... ok
	Doctest: pyzufall.generator.sprichwort ... ok
	Doctest: pyzufall.generator.stadt ... ok
	Doctest: pyzufall.generator.stadt_bl ... ok
	Doctest: pyzufall.generator.tier ... ok
	Doctest: pyzufall.generator.trinken ... ok
	Doctest: pyzufall.generator.verbd ... ok
	Doctest: pyzufall.generator.verbi ... ok
	Doctest: pyzufall.generator.verbi2 ... ok
	Doctest: pyzufall.generator.verbn ... ok
	Doctest: pyzufall.generator.verbt ... ok
	Doctest: pyzufall.generator.verbt2 ... ok
	Doctest: pyzufall.generator.vorname_m ... ok
	Doctest: pyzufall.generator.vorname_w ... ok
	Doctest: pyzufall.generator.wort ... ok
	Doctest: pyzufall.generator.zahl ... ok
	Doctest: pyzufall.helfer.erste_gross ... ok
	Doctest: pyzufall.helfer.lese ... ok
	Doctest: pyzufall.helfer.str_add ... ok
	test.test_satz ... ok
	test.test_satz_frage ... ok
	test.test_sprichwort ... ok
	
	----------------------------------------------------------------------
	Ran 45 tests in 0.907s
	
	OK

.. note::

    Für die Unittests wird `nose <https://nose.readthedocs.org/en/latest/>`_ verwendet und muss installiert sein.

Entwicklerversion installieren
------------------------------
::

	$ sudo python3 setup.py install

.. warning::

	Diese Version ist nicht für den produktiven Einsatz gedacht.
	Sie sollte nur zum Entwickeln oder zu Testzwecken eingesetzt werden.

Vor dem Release
---------------

- Versionsnummer in :mod:`version.py` überprüfen
- :doc:`changelog` aktualisieren, Versionsnummer und Datum überprüfen
- Unittests ausführen::

	$ make test

- Dokumentation bauen und überprüfen::

	$ make docs

Release
-------

- letzte Änderungen in git einchecken
- git tag mit Versionsnummer setzen
- push auf github
- auf PyPI veröffentlichen::

	$ python3 setup.py sdist upload

Nach dem Release
----------------

- Versionsnummer inkrementieren + 'dev'
- am nächsten Release arbeiten :)
