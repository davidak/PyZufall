Die Python-Bibliothek **PyZufall** beinhaltet diverse Funktionen für das **Generieren zufälliger Daten** wie Namen, Berufe, Bandnamen, ein Datum, Sätze oder den kompletten Datensatz einer Personen.

Die Entwicklung begann als Satzgenerator für http://satzgenerator.de/ und wird noch in diese Richtung weitergeführt.
Sie soll aber auch eine generelle Sammlung von Funktionen zur Generierung zufälliger Daten darstellen.
So wird sie schon von `anderen Projekten <https://pyzufall.readthedocs.org/de/latest/benutzer.html>`_ verwendet, wie dem `Random VCard-Generator <https://github.com/davidak/random-vcard-generator>`_.

**PyZufall** ist `freie und Open Source Software <http://www.gnu.org/philosophy/free-sw.de.html>`_. Es steht unter der `GPL Version 3 <http://www.gnu.org/licenses/gpl-3.0.html>`_.

Den Quelltext findest du im `Repository <https://github.com/davidak/pyzufall>`_ und Fehler sowie Verbesserungsvorschläge werden im `Bugtracker <https://github.com/davidak/pyzufall/issues>`_ gesammelt.

Jeder ist eingeladen zum Projekt beizutragen!

Ausführliche Informationen sind in der `Dokumentation <https://pyzufall.readthedocs.org/>`_ zu finden.

Installation
------------

Mit `pip <http://www.pip-installer.org/en/latest/installing.html>`_ kannst du die neuste stabile Version von **PyZufall** ganz einfach auf deinem System installieren::

	$ sudo pip install pyzufall

Meist ruft der Befehl pip für Python 2.x auf. PyZufall wird hauptsächlich für Python 3 entwickelt, bei einem schnellen Test mit Python 2.6.x und 2.7.x sind allerdings keine Fehler aufgefallen.

Pip für **Python 3** wird auf vielen System (z.B OS X oder Ubuntu) wie folgt ausgeführt::

	$ sudo pip-3.2 install pyzufall

Oder du installierst **PyZufall** manuell, indem du die neuste Version von `PyPI <https://pypi.python.org/pypi/pyzufall>`_ runterlädst, diese entpackst und installierst.
::
	
	$ tar -xzf PyZufall-0.11.tar.gz
	$ cd PyZufall-0.11/
	$ sudo python3 setup.py install

Verwenden
---------

Hier ein einfaches Beispiel, wie du mit PyZufall einen zufälligen Namen generieren kannst::

	from pyzufall.generator import vorname_m, nachname
	name = vorname_m() + ' ' + nachname()
	print(name)

Mehr zur Verwendung der einzelnen Module und deren Funktionen erfährst du in der `Dokumentation <https://pyzufall.readthedocs.org/de/latest/verwenden.html>`_.
