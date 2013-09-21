Installation
============

Die aktuellste Version von **pyzufall** findest du auf `github <https://github.com/davidak/pyzufall>`_.

Eine stabile Version wird es auf `PyPI <https://pypi.python.org/>`_ geben.

.. note:: Derzeit befindet sich **pyzufall** in aktiver Entwicklung. Daher kann sich die Struktur oder Funktionsnamen noch ändern.

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

    imac:pyzufall davidak$ nosetests -v
    test.test_test ... ok
    test_helfer.test_lese ... ok
    test_helfer.test_erste_gross ... ok
    test_satz.test_satz ... ok
    test_satz.test_satz_frage ... ok
    
    ----------------------------------------------------------------------
    Ran 5 tests in 0.822s
    
    OK

.. note::

    Für die Unittests wird `nose <https://nose.readthedocs.org/en/latest/>`_ verwendet und muss installiert sein.
