Verwenden
=========

Importieren
-----------

Um :py:mod:`pyzufall` verwenden zu können, muss es importiert werden::

    >>> import pyzufall as z

Beispiele
---------

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
