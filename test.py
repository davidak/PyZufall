#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pyzufall as z

print("\nTestscript für die Klasse PyZufall\n")
print("Person: "+z.person())
print("Berufsbezeichnung: "+z.beruf())
print("Essen: "+z.essen(0))
print("Essen2: "+z.essen(2))
print("Beilage: "+z.beilage())
print("Trinken: "+z.trinken())
print("Stadt: "+z.stadt())
print("Ort: "+z.ort())
print("Band: "+z.band())
print("Bandart: "+z.bandart())
print("Wort: "+z.wort())
print("Zahl: "+z.zahl())
print("Farbe: "+z.farbe())
print("Datum: "+z.datum())
print("Sprichwort: "+z.sprichwort())
print("Satz: "+z.satz()+"\n")

for i in range(1,11):
	print(str(i) + ". " + z.satz())