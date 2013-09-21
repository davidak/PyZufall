Entwicklung
===========

Bei der Entwicklung von **pyzufall** wird `git <http://git-scm.com/>`_ für die Versionierung eingesetzt.

Die Dokumentation wird mit `Sphinx <http://sphinx-doc.org/>`_ erzeugt und die Unittests durch `nose <http://nose.readthedocs.org/>`_ ausgeführt.

Repository
----------

https://github.com/davidak/pyzufall

Vor dem Release
---------------

- Versionsnummer in :mod:`version.py` überprüfen
- :doc:`changelog` aktualisieren, Versionsnummer und Datum
- Unittests ausführen::

	$ nosetests -v

- Dokumentation bauen::

	$ make html
	$ make latexpdf

Release
-------

- letzte Änderungen in git einchecken
- git tag mit Versionsnummer setzen
- push auf github
- auf PyPI veröffentlichen::

	$ python setup.py sdist upload

Nach dem Release
----------------

- Versionsnummer inkrementieren
- am nächsten Release arbeiten :)