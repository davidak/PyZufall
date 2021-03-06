Verwenden
=========

Anhand von Beispielen werden die verschiedenen Module von **PyZufall** vorgestellt.

Name generieren
---------------

Um einen Namen zu generieren wird das Modul :py:mod:`pyzufall.generator` verwendet, dass eine Vielzahl von Funktionen für das Generieren von Daten bereitstellt.

::

    from pyzufall.generator import vorname, nachname
    name = vorname() + ' ' + nachname()
    print(name)

.. code-block:: none

    Samira Reschke

.. seealso::

    Eine Übersicht aller Funktionen findest du in der :doc:`Referenz <module>`.

Mahlzeit zusammenstellen
------------------------

Indem du mehrere Funktionen kombinierst, kannst du eine ganze Mahlzeit generieren.

::

    from pyzufall.generator import essen, beilage, trinken
    s = "Heute Abend gibt es {} mit {} und dazu ein Glas {}.".format(essen(), beilage(), trinken())
    print(s)

.. code-block:: none

    Heute Abend gibt es Salzkartoffeln mit Rösti und dazu ein Glas Zuckerschnaps.

Meine Band
----------

Auch Funktionen für eine Band gibt es.

::

    from pyzufall.generator import bandart, band, vorname
    s = "Meine {} heißt '{}' und besteht aus {}, {} und mir.".format(bandart(), band(), vorname(), vorname())
    print(s)

.. code-block:: none

    Meine Ambientband heißt 'Enten bei den Affen im Zoo' und besteht aus Dietmar, Kira und mir.

Satz generieren
---------------

Das Modul :py:mod:`pyzufall.satz` generiert zufällige Sätze nach diversen Schemata.

::

    from pyzufall.satz import satz
    s = satz()
    print(s)

.. code-block:: none

    Der anonyme Vater fällt auf dem Straßenfest auf.

Es kann auch eine spezielle Art von Satz generiert werden.

::

    from pyzufall.satz import satz_absurde_farbfunktion
    s = satz_absurde_farbfunktion()
    print(s)

.. code-block:: none

    Violett ist aggressiver als Gelb.

Person generieren
-----------------

Die Klasse :py:class:`Person <pyzufall.person.Person>` des Moduls :py:mod:`pyzufall.person` generiert eine Person mit diversen Daten. Du kannst den Datensatz der Person ausgeben oder direkt auf jede einzelne Variable zugreifen.

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
    Name: Fred Wittke (die_taube)
    Geburtsname: Dornemann
    Geschlecht: männlich
    Geburtsdatum: 06.01.1912 (103)
    Geburtsort: Wittlich
    Wohnort: Kaltenkirchen
    Beruf: Rentner
    E-Mail: fred@die-taube.de
    Homepage: http://die-taube.de/
    Interessen: Brieftauben züchten
    Lieblingsfarbe: Gelb
    Lieblingsessen: Frischbraten mit Röstzwiebeln
    Motto: Reden ist Silber, Schweigen ist Gold.
    ********************************************************************************
    
    Fred und Franz sitzen auf einer Bank im Park.
    Fred (103) wohnt in Kaltenkirchen und isst gerne Frischbraten mit Röstzwiebeln.

Ein praktischer Einsatszweck dafür ist der `Random VCard-Generator <https://github.com/davidak/random-vcard-generator>`_.
