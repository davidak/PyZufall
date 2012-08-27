#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

# Daten aus Dateien einlesen
vornamen = open('data/vornamen', 'r').read().splitlines()
verb = open('data/verb', 'r').read().splitlines()
verb2 = open('data/verb2', 'r').read().splitlines()
adj = open('data/adjektiv', 'r').read().splitlines()
ort = open('data/ort', 'r').read().splitlines()


def person():
	beziehung_m = ['Vater', 'Bruder', 'Mann', 'Sohn', 'Onkel', 'Opa', 'Cousin', 'Enkel', 'Chef', 'Freund', 'Partner', 'Kollege', 'Mitarbeiter', 'Mitbewohner', 'Vermieter', 'Lehrer']
	beziehung_w = ['Mutter', 'Schwester', 'Frau', 'Tochter', 'Tante', 'Oma', 'Cousine', 'Enkelin', 'Cheffin', 'Freundin', 'Partnerin', 'Kollegin', 'Mitarbeiterin', 'Mitbewohnerin', 'Vermieterin', 'Lehrerin']
	spezial = ['Er', 'Sie', 'Es', 'Jemand', 'Niemand', 'Ein Held', 'Ein Penner', 'Ein Verkäufer', 'Ein Zuhälter', 'Eine Prostituierte', 'Eine Nutte', 'Eine Hure', 'Eine Schlampe', 'Ein Lehrer', 'Ein Polizist', 'Ein Beamter', 'Ein Arzt', 'Hitler', 'Ein Bernd', 'Ein Schwuler', 'Ein Behinderter', 'Die Sekretärin', 'Der Affenmensch', 'Die Transe', 'Das Mannsweib', 'Das Penismädchen', 'Die Lesbe', 'Die Kampflesbe', 'Der Satanist', 'Der Alkoholiker', 'Ein normaler Mensch']
	possessivpronomen_m = ['Mein', 'Dein', 'Sein', 'Ihr']

	# Person generieren
	z = random.randint(1,10)
	if z == 1:
		person = random.choice(vornamen) + 's ' + random.choice(beziehung_m)
	elif z == 2:
		person = random.choice(vornamen) + 's ' + random.choice(beziehung_w)
	elif z == 3:
		person = random.choice(possessivpronomen_m) + ' ' + random.choice(beziehung_m)
	elif z == 4:
		person = random.choice(possessivpronomen_m) + 'e ' + random.choice(beziehung_w)
	elif z == 5:
		person = 'Der ' + random.choice(beziehung_m)
	elif z == 6:
		person = 'Die ' + random.choice(beziehung_w)
	elif z == 7:
		person = random.choice(spezial)
	else:
		person = random.choice(vornamen)
	return person

