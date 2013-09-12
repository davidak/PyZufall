Installation
============

Die aktuellste Version findest du auf `github <https://github.com/davidak/pyzufall>`_. Eine stabile Version wird es auf `PyPI <https://pypi.python.org/>`_ geben.

Manuelle Installation
---------------------

Klone das git-Repository in dein Projekt-Verzeichnis::

    $ mkdir meinprojekt
    $ cd meinprojekt
    $ git clone https://github.com/davidak/pyzufall.git

Unittests
---------

Um den Code auf deinem System zu testen, führe folgenden Befehl im Ordner von :py:mod:`pyzufall` aus::

    $ nosetests -v
    pyzufall.test.test_satz ... ok
    pyzufall.test.test_test ... ok
    pyzufall.test.test_lese ... ok
    pyzufall.test.test_ersten_buchstaben_gross ... ok
    
    ----------------------------------------------------------------------
    Ran 4 tests in 0.534s
    
    OK

Für die Unittests wird `nose <https://nose.readthedocs.org/en/latest/>`_ benutzt und muss installiert sein.
