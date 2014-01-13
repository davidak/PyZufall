Verwenden
=========

Anhand von Beispielen werden die verschiedenen Module von **PyZufall** vorgestellt.

Name generieren
---------------

Um einen Namen zu generieren wird das Modul :py:mod:`pyzufall.generator` verwendet, dass eine Vielzahl von Funktionen für das Generieren von Daten bereitstellt.

::

    from pyzufall.generator import vorname_m, nachname
    name = vorname_m() + ' ' + nachname()
    print(name)

.. seealso::

    Eine Übersicht aller Funktionen findest du in der :doc:`Referenz <module>`.

Satz generieren
---------------

Das Modul :py:mod:`pyzufall.satz` generiert zufällige Sätze nach diversen Schemata.

::

    from pyzufall.satz import satz
    satz = satz()
    print(satz)

Person generieren
-----------------

Die Klasse :py:class:`Person <pyzufall.person.Person>` des Moduls :py:mod:`pyzufall.person` generiert eine Person mit diversen Daten. Du kannst alle Daten der Person aufeinmal ausgeben oder direkt auf jede einzelne Variable zugreifen.

::

    from pyzufall.person import Person
    p1 = Person()
    p2 = Person()
    
    print(p1)
    
    print("{} und {} sitzen auf einer Bank im Park.".format(p1.vorname, p2.vorname))
    print("{} ({}) wohnt in {} und isst gerne {}.".format(p1.vorname, p1.alter, p1.wohnort, p1.lieblingsessen))
    
    del p1, p2

.. code-block:: none

    ********************************************************************************
    Name: Tilmann Ried
    Geschlecht: männlich
    Geburtsdatum: 19.04.1981 (32)
    Geburtsort: Schwelm
    Wohnort: Starnberg
    Beruf: arbeitslos
    Interessen: Sonnenstudio, Mofatuning
    Lieblingsfarbe: Grün
    Lieblingsessen: Schokoladen
    Motto: Du sollst den Tag nicht vor dem Abend loben.
    ********************************************************************************
    
    Tilmann und Emre sitzen auf einer Bank im Park.
    Tilmann (32) wohnt in Starnberg und isst gerne Schokoladen.

Ein praktischer Einsatszweck dafür ist der `Random VCard-Generator <https://github.com/davidak/random-vcard-generator>`_.