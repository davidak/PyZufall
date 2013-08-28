#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pyzufall as z
import person as p

print("\nDemoscript für das Modul pyzufall " + z.__version__)
print('-' * 37 + "\n")
print("Person: "+z.person())
print("Berufsbezeichnung M: "+z.beruf_m())
print("Berufsbezeichnung W: "+z.beruf_w())
print("Essen: "+z.essen())
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

p1 = p.Person()
print(p1)
p2 = p.Person()
print(p2)
del p1
del p2