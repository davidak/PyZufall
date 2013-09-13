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

Um den Code auf deinem System zu testen, führe folgenden Befehl im Projekt-Verzeichnis aus::

    $ nosetests -v
    test.test_satz ... ok
    test.test_satz_frage ... ok
    test.test_test ... ok
    test.test_lese ... ok
    test.test_erste_gross ... ok
    
    ----------------------------------------------------------------------
    Ran 5 tests in 0.807s
    
    OK

Für die Unittests wird `nose <https://nose.readthedocs.org/en/latest/>`_ verwendet und muss installiert sein.
