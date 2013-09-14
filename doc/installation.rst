Installation
============

Die aktuellste Version von **pyzufall** findest du auf `github <https://github.com/davidak/pyzufall>`_. Eine stabile Version wird es auf `PyPI <https://pypi.python.org/>`_ geben.

Manuelle Installation
---------------------

Klone das git-Repository::

    $ git clone https://github.com/davidak/pyzufall.git

.. note::

    Dafür muss `git <http://git-scm.com/>`_ installiert sein.

Danach kopierst du das Paket **pyzufall** in dein Projekt-Verzeichnis::

    $ mkdir meinprojekt
    $ mv pyzufall/pyzufall meinprojekt
    $ cd meinprojekt

Unittests
---------

Um den Code auf deinem System zu testen, führe folgenden Befehl im heruntergeladenen Repository aus::

    $ nosetests -v
    test.test_satz ... ok
    test.test_satz_frage ... ok
    test.test_test ... ok
    test.test_lese ... ok
    test.test_erste_gross ... ok
    
    ----------------------------------------------------------------------
    Ran 5 tests in 0.807s
    
    OK

.. note::

    Für die Unittests wird `nose <https://nose.readthedocs.org/en/latest/>`_ verwendet und muss installiert sein.
