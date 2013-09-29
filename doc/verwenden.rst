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
    print(p1.vorname + " und " + p2.vorname + " sitzen auf einer Bank im Park.\n")
    print(p2.vorname + " (" + str(p2.alter) + ") wohnt in " + p2.wohnort + ".")

.. code-block:: none

    ********************************************************************************
    Name: Kornelia Eismann
    Geschlecht: weiblich
    Geburtsdatum: 27.04.1974 (39)
    Geburtsort: Geesthacht
    Wohnort: Halle
    Beruf: Technische Zeichnerin
    Interessen: Würfelspiele
    Lieblingsfarbe: Weiß
    Lieblingsessen: Steak
    Motto: Augen auf beim Eierkauf.
    ********************************************************************************
    
    Kornelia und Thorge sitzen auf einer Bank im Park.
    
    Thorge (58) wohnt in Stadthagen.

Ein praktischer Einsatszweck dafür ist der `Python Random VCard-Generator <https://github.com/davidak/python-random-vcard-generator>`_.