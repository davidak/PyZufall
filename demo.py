#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pyzufall import __version__
from pyzufall.generator import adjektiv, band, bandart, baum, beilage, beruf_m, beruf_w, color, datum, essen, farbe, firma, geburtsdatum, gegenstand, interesse, koerperteil, nachname, objekt, objekt_m, objekt_w, ort, person, person_m, person_objekt_m, person_objekt_w, person_w, pflanze, sprichwort, stadt, stadt_bl, tier, trinken, verbd, verbi, verbi2, verbn, verbt, verbt2, vorname, vorname_m, vorname_w, wort, zahl
from pyzufall.satz import satz
from pyzufall.person import Person

titel = "Demoscript für PyZufall " + __version__
print("\n" + titel + "\n" + '~' * len(titel) + "\n")
print("Person: " + person())
print("Berufsbezeichnung M: " + beruf_m())
print("Berufsbezeichnung W: " + beruf_w())
print("Essen: " + essen())
print("Beilage: " + beilage())
print("Trinken: " + trinken())
print("Stadt: " + stadt())
print("Ort: " + ort())
print("Band: " + band())
print("Bandart: " + bandart())
print("Wort: " + wort())
print("Zahl: " + zahl())
print("Farbe: " + farbe())
print("Datum: " + datum())
print("Sprichwort: " + sprichwort())

anzahl = 10
print("\n" + str(anzahl) + " zufällige Sätze:\n")

for i in range(1,anzahl+1):
	print(str(i) + ". " + satz())
print() # Leerzeile

print("Zufällige Personen generieren:\n")
p1 = Person()
print(p1)
p2 = Person()
print(p2)

print("{} und {} sitzen auf einer Bank im Park.\n".format(p1.vorname, p2.vorname))

del p1
del p2