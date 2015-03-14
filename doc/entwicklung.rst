Entwicklung
===========

Bei der Entwicklung von **PyZufall** wird `git <http://git-scm.com/>`_ für die Versionierung eingesetzt.

Die Dokumentation wird mit `Sphinx <http://sphinx-doc.org/>`_ erzeugt und die Unittests durch `nose <http://nose.readthedocs.org/>`_ ausgeführt.

Code Status
-----------

Hier wird das Ergebnis der automatischen Unittests und die `Coverage <http://de.wikipedia.org/wiki/Testabdeckung#Testabdeckung_in_der_Softwaretechnik>`_ des Codes im Repository angezeigt:

.. image:: https://travis-ci.org/davidak/PyZufall.svg?branch=master
    :target: https://travis-ci.org/davidak/PyZufall

.. image:: https://coveralls.io/repos/davidak/PyZufall/badge.svg?branch=master
  :target: https://coveralls.io/r/davidak/PyZufall?branch=master

Repository runterladen
----------------------
::

	$ git clone https://github.com/davidak/pyzufall.git

Dokumentation erzeugen
----------------------

Mit folgendem Befehl wird die HTML-Version sowie LaTeX samt PDF erzeugt.
::

	$ make docs

Einzeln geht das mit::

	$ make html
	$ make pdf

Unittests ausführen
-------------------

Um den Code auf deinem System zu testen, führe folgenden Befehl im heruntergeladenen Repository aus::

	imac:PyZufall davidak$ nosetests --with-doctest
	..................................................
	----------------------------------------------------------------------
	Ran 50 tests in 0.867s

	OK

Vor dem Release
---------------

- Versionsnummer in :mod:`version.py` überprüfen, niemals 'dev' auf PyPI laden!
- :doc:`changelog` aktualisieren, Versionsnummer und Datum überprüfen
- Unittests ausführen::

	$ nosetests --with-doctest

- Dokumentation bauen und überprüfen::

	$ make docs

- Installation von PyPI mit pip testen: `<https://wiki.python.org/moin/TestPyPI>`_

  Paket nach testpypi hochladen:
  ::

	$ python3 setup.py sdist upload -r https://testpypi.python.org/pypi

  Prüfen auf Syntax-Fehler in der README: https://testpypi.python.org/pypi/PyZufall

  Einmal testweise installieren:
  ::

	$ pip install -i https://testpypi.python.org/pypi <package name>

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
