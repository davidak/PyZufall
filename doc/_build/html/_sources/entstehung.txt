Entstehung
==========

Das Spiel
---------

Als Kind hatte ich bei meiner Oma öfter das Spiel `Opa plätschert lustig in der Badewanne <http://www.mama-tipps.de/tipp/Opa-plaetschert-Badewanne.html>`_ gespielt.

Dabei hat jeder Spieler ein Blatt Papier, dass er quer nimmt und als erstes einen Namen oder eine Person darauf schreibt, es an der Stelle faltet, so dass man es nicht mehr lesen kann und es im Uhrzeigersinn weitergibt. Dann schreibt jeder auf das erhaltene Blatt ein Verb, gibt es weiter und schribt ein Adjektiv und nach nochmaligem Weitergeben einen Ort darauf.

So entstehen absurde und zufällige Sätze. Das war immer sehr witzig.

Das Programm
------------

Als ich älter wurde, begann ich Programmieren zu lernen. Dabei hat mich immer begeistert, durch Zufall etwas zu generieren, was teilweise einen Sinn ergibt, aber oft sehr absurd und dadurch lustig ist.

So ist ein `Personendatengenerator <http://davidak.de/wiki/perl/personendatengenerator>`_ entstanden, mit dem eine `Personendatenbank <http://davidak.de/personen/>`_ befüllt wurde.

Auch hab ich ein Script geschrieben, dass Sätze nach dem Muster des Spiels generiert. Erst in Perl und dann in Python. Diese Sätze werden natürlich auf Dauer langweilig.

Da mittlerweile Python die Programmiersprache meiner Wahl ist, habe ich das Script darin weiterentwickelt, mit diversen Satz-Schemata und anderen tollen Funktionen.

Der Satzgenerator
-----------------

Inzwischen gibt es `satzgenerator.de <http://satzgenerator.de/>`_. Auf dieser Webseite werden zufällige Sätze generiert, die bewertet und geteilt werden können.

Für die Generierung der Sätze wird `pyzufall <https://github.com/davidak/pyzufall>`_ genutzt. Die Seite ist auch in Python programmiert, benutzt das Web-Framework `Bottle <http://bottlepy.org/>`_ und eine MySQL-Datenbank für die Speicherung der Sätze und Bewertungen.

Pyzufall ist Open Source und wird bereits für :doc:`andere Projekte <benutzer>` benutzt.
