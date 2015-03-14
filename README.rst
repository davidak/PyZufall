Die Python-Bibliothek **PyZufall** beinhaltet diverse Funktionen für das **Generieren zufälliger Daten**.

Die Entwicklung begann als Satzgenerator für http://satzgenerator.de/ und wird noch in diese Richtung weitergeführt.
Sie soll aber auch eine generelle Sammlung von Funktionen zur Generierung zufälliger Daten darstellen.
So wird sie schon von `anderen Projekten <https://pyzufall.readthedocs.org/de/latest/benutzer.html>`_ verwendet, wie dem `Random VCard-Generator <https://github.com/davidak/random-vcard-generator>`_.

**PyZufall** ist `freie Software <http://www.gnu.org/philosophy/free-sw.de.html>`_. Der Quellcode ist Open Source und steht unter der `GPL Version 3 <http://www.gnu.org/licenses/gpl-3.0.html>`_.

Python 3 wird offiziell unterstützt, Informationen zur `Python 2.7 Kompatibilität <https://pyzufall.readthedocs.org/en/latest/python27.html>`_ gibt es in der Doku.

Den Quelltext findest du im `Repository <https://github.com/davidak/pyzufall>`_ und Fehler sowie Verbesserungsvorschläge werden im `Bugtracker <https://github.com/davidak/pyzufall/issues>`_ gesammelt.

Jeder ist eingeladen zum Projekt beizutragen!

Ausführliche Informationen sind in der `Dokumentation <https://pyzufall.readthedocs.org/>`_ zu finden.

Installation
------------

Mit der Paketverwaltung `pip <http://www.pip-installer.org/en/latest/>`_ lässt sich die neuste stabile Version installieren.
::

	# pip install pyzufall

Verwenden
---------

Hier ein einfaches Beispiel, wie du mit **PyZufall** einen zufälligen Namen generieren kannst::

	from pyzufall.generator import vorname_m, nachname
	name = vorname_m() + ' ' + nachname()
	print(name)

In der Dokumentation findest du `weitere Beispiele <https://pyzufall.readthedocs.org/en/latest/verwenden.html>`_ und eine `Referenz aller Funktionen <https://pyzufall.readthedocs.org/en/latest/module.html>`_.
