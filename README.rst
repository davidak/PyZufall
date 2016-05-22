Die Python-Bibliothek **PyZufall** beinhaltet Funktionen für das **Generieren zufälliger Daten**.

Die Entwicklung begann als `Satzgenerator <http://satzgenerator.de/>`_ und wird noch in diese Richtung weitergeführt. Durch die große Sammlung an Funktionen kann sie inzwischen vielfältig eingesetzt werden. So wird sie bereits von `anderen Projekten <https://pyzufall.readthedocs.org/de/latest/benutzer.html>`_ verwendet, wie dem `Random VCard-Generator <https://github.com/davidak/random-vcard-generator>`_.

**PyZufall** ist `Freie Software <http://fsfe.org/about/basics/freesoftware.de.html>`_. Der Quellcode ist Open Source und steht unter der `GPL Version 3 <http://www.gnu.org/licenses/gpl-3.0.html>`_.

Das `Code Repository <https://github.com/davidak/pyzufall>`_ und ein `Bugtracker <https://github.com/davidak/pyzufall/issues>`_ sind auf Github.

Jeder ist eingeladen zum Projekt beizutragen!

Ausführliche Informationen sind in der `Dokumentation <https://pyzufall.readthedocs.org/>`_ zu finden.

Installation
------------

Mit der Paketverwaltung `pip <http://www.pip-installer.org/de/latest/>`_ lässt sich die neuste stabile Version installieren.
::

	# pip install pyzufall

Kompatibel mit Python 2.7, Python 3.3+ sowie `PyPy <http://pypy.org/>`_.

Verwenden
---------

Hier ein einfaches Beispiel, wie du mit **PyZufall** einen zufälligen Namen generieren kannst::

	from pyzufall.generator import vorname, nachname
	name = vorname() + ' ' + nachname()
	print(name)

In der Dokumentation findest du `weitere Beispiele <https://pyzufall.readthedocs.org/de/latest/verwenden.html>`_ und eine `Referenz aller Funktionen <https://pyzufall.readthedocs.org/de/latest/module.html>`_.
