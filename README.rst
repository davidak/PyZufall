Die Python-Bibliothek **PyZufall** beinhaltet diverse Funktionen für das **Generieren zufälliger Daten**.

Die Entwicklung begann als Satzgenerator für http://satzgenerator.de/ und wird noch in diese Richtung weitergeführt.
Sie soll aber auch eine generelle Sammlung von Funktionen zur Generierung zufälliger Daten darstellen.
So wird sie schon von `anderen Projekten <https://pyzufall.readthedocs.org/de/latest/benutzer.html>`_ verwendet, wie dem `Random VCard-Generator <https://github.com/davidak/random-vcard-generator>`_.

**PyZufall** ist `freie Software <http://www.gnu.org/philosophy/free-sw.de.html>`_. Der Quellcode ist Open Source und steht unter der `GPL Version 3 <http://www.gnu.org/licenses/gpl-3.0.html>`_.

Als `Repository <https://github.com/davidak/pyzufall>`_ und `Bugtracker <https://github.com/davidak/pyzufall/issues>`_ wird Github benutzt.

Ausführliche Informationen sind in der `Dokumentation <https://pyzufall.readthedocs.org/>`_ zu finden.

Installation
------------

Mit der Paketverwaltung `pip <http://www.pip-installer.org/en/latest/>`_ lassen sich Python-Pakete aus dem `Python Package Index <https://pypi.python.org/pypi/vcardgen/>`_ (PyPI) installieren.
::

	# pip install pyzufall

Verwenden
---------

Hier ein einfaches Beispiel, wie du mit PyZufall einen zufälligen Namen generieren kannst::

	from pyzufall.generator import vorname_m, nachname
	name = vorname_m() + ' ' + nachname()
	print(name)
