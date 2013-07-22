.. pyzufall documentation master file, created by
   sphinx-quickstart on Mon Jul 22 21:52:45 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Dokumentation von pyzufall
==========================

Das Python-Modul :py:mod:`pyzufall` hat viele Funktionen, um diverse Daten zu erzeugen.

Die komplexeste ist dabei :py:func:`pyzufall.satz`, mit der sich zufällige Sätze generieren lassen.

Es bildet die Grundlage für `satzgenerator.de <http://satzgenerator.de/>`_.

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

Eine zufällige männliche Person erzeugen.person_m`::

    >>> print(z.person_m())
    der verdorbene Sohn

Eine zufällige Stadt erzeugen::

    >>> print(z.stadt())
    Lörrach

Ein Fantasiewort erzeugen::

    >>> print(z.wort())
    Maugodno

Diese Funktion kann auch verwendet werden, um sich einen Nickname oder Künstlernamen zu erzeugen.

Ein zufälliges Sprichwort erzeugen::

    >>> print(z.sprichwort())
    Das schlägt dem Fass den Boden aus.


Ein Essen erzeugen::

    >>> print(z.essen(1))
    Süßholzkekse

Ein Getränk erzeugen::

    >>> print(z.trinken())
    Haselnusskaffee

Und schlussendlich die Funktion, welche die meisten der anderen benutzt, um ganze Sätze zu generieren.
Dabei sind diverse Satz-Schemata hinterlegat, sodass es nicht langweilig wird.

Hier einige Beispiele::

    >>> print(z.satz())
    Weshalb katasysiert der witzige Wolfram fantasielos unter der Brücke?
    >>> print(z.satz())
    Die Lehrerin zersägt deine Rosskastanie.
    >>> print(z.satz())
    Der Kollege programmiert deine Partnerin im Atomkraftwerk.
    >>> print(z.satz())
    Heinrich gewinnt den Ahorn heimtückisch auf einer Hochzeit.
