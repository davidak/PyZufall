.. pyzufall documentation master file, created by
   sphinx-quickstart on Mon Jul 22 21:52:45 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Dokumentation von pyzufall
==========================

Das Python-Modul :py:mod:`pyzufall` hat viele Funktionen, um diverse Daten zu erzeugen.

Die komplexeste ist dabei :py:func:`pyzufall.satz`, mit der sich zufällige Sätze generieren lassen.

Es wurde für `satzgenerator.de <http://satzgenerator.de/>`_ entwickelt, kann aber vielfältig eingesetzt werden.

Installation
============

Die aktuellste Version findest du auf `github <https://github.com/davidak/pyzufall>`_. Eine stabile Version wird es auf `PyPI <https://pypi.python.org/>`_ geben.

Klone das git-Repository in dein Projekt-Verzeichnis::

    $ mkdir meinprojekt
    $ cd meinprojekt
    $ git clone https://github.com/davidak/pyzufall.git

Verwendung
==========

Um :py:mod:`pyzufall` verwenden zu können, muss es importiert werden::

    >>> import pyzufall as z

Beispiele
=========

Einen zufälligen männlichen Vornamen erzeugen::

    >>> print(z.vorname_m())
    Magnus

Einen zufälligen weiblichen Vorname mit Nachname erzeugen::

   >>> print(z.vorname_w() + ' ' + z.nachname())
   Carmen Büchler

Ein zufälliges Sprichwort erzeugen::

    >>> print(z.sprichwort())
    Das schlägt dem Fass den Boden aus.



Die Funktion :py:func:`pyzufall.satz` benutzt die meisten anderen Funktionen, um ganze Sätze zu generieren.
Es sind viele Satz-Schemata hinterlegt für abwechlungsreiche Ergebnisse.

Hier einige Beispiele::

    >>> print(z.satz())
    Weshalb katasysiert der witzige Wolfram fantasielos unter der Brücke?
    >>> print(z.satz())
    Die Lehrerin zersägt deine Rosskastanie.
    >>> print(z.satz())
    Der Kollege programmiert deine Partnerin im Atomkraftwerk.
    >>> print(z.satz())
    Heinrich gewinnt den Ahorn heimtückisch auf einer Hochzeit.

Eine Übersicht aller Funktionen findest du in der Referenz:  :py:mod:`pyzufall`

Benutzer
========

Hier ist eine Liste mit Projekten, die :py:mod:`pyzufall` verwenden:

* `satzgenerator.de <http://satzgenerator.de/>`_
* `Python Random VCard-Generator <https://github.com/davidak/python-random-vcard-generator>`_

Dein Projekt füge ich auch gerne hinzu.

Auch über Rückmeldungen jeder Art freue ich mich.

Einfach eine E-Mail an post at davidak punkt de oder das `Kontaktformular <http://davidak.de/kontakt>`_ benutzen.