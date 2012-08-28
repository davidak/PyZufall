#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

random.seed() # Zufallsgenerator initialisieren

# Daten aus Dateien einlesen
vornamen_m = open('data/vornamen_m', 'r').read().splitlines()
vornamen_w = open('data/vornamen_w', 'r').read().splitlines()
vornamen = vornamen_m + vornamen_w
nachnamen = open('data/nachnamen', 'r').read().splitlines()
geschmack = open('data/geschmack', 'r').read().splitlines()
nahrung = open('data/nahrung', 'r').read().splitlines()
ns = open('data/nebensatz', 'r').read().splitlines()
verb = open('data/verb', 'r').read().splitlines()
verb2 = open('data/verb2', 'r').read().splitlines()
adj = open('data/adjektiv', 'r').read().splitlines()
ort = open('data/ort', 'r').read().splitlines()
stadte = open('data/stadt_bundesland', 'r').read().splitlines()
beruf = open('data/berufe', 'r').read().splitlines()
musik = open('data/musikgenre', 'r').read().splitlines()

# ECHO50: 50% Chance, dass das übergebene Wort zurückgegeben wird
def e5(wort):
	if random.randint(0,1):
		return wort
	else:
		return ''


# Person generieren
beziehung_m = ['Vater', 'Bruder', 'Mann', 'Sohn', 'Onkel', 'Opa', 'Cousin', 'Enkel', 'Chef', 'Freund', 'Partner', 'Kollege', 'Mitarbeiter', 'Mitbewohner', 'Vermieter', 'Lehrer']
beziehung_w = ['Mutter', 'Schwester', 'Frau', 'Tochter', 'Tante', 'Oma', 'Cousine', 'Enkelin', 'Cheffin', 'Freundin', 'Partnerin', 'Kollegin', 'Mitarbeiterin', 'Mitbewohnerin', 'Vermieterin', 'Lehrerin']
spezial = ['Er', 'Sie', 'Es', 'Jemand', 'Niemand', 'Ein Held', 'Ein Penner', 'Ein Verkäufer', 'Ein Zuhälter', 'Eine Prostituierte', 'Eine Nutte', 'Eine Hure', 'Eine Schlampe', 'Ein Lehrer', 'Ein Polizist', 'Ein Beamter', 'Ein Arzt', 'Hitler', 'Ein Bernd', 'Ein Schwuler', 'Ein Behinderter', 'Die Sekretärin', 'Der Affenmensch', 'Die Transe', 'Das Mannsweib', 'Das Penismädchen', 'Die Lesbe', 'Die Kampflesbe', 'Der Satanist', 'Der Alkoholiker', 'Ein normaler Mensch']
possessivpronomen_m = ['Mein', 'Dein', 'Sein', 'Ihr']

def person():
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


# Wort
vokal = ['a', 'e', 'i', 'o', 'u', 'ei', 'au']
konsonant = ['b', 'c', 'd', 'f', 'g', 'h', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'sch']
konsonant2 = ['h', 'k', 'l', 'm', 'n', 's', 't']

def wort():
	laenge = random.randint(3,12)
	anfaengt = random.randint(1,3)
	text = ""
	
	if anfaengt == 2: # Anfang wird ein Vokal
		text = random.choice(vokal)
		while len(text) < laenge:
			text += random.choice(konsonant)
			if len(text) < laenge and random.randint(0,1):
				text += random.choice(konsonant2)
			if len(text) >= laenge:
				break
			text += random.choice(vokal)

	else: # Anfang wird ein Konsonant
		text = random.choice(konsonant)
		while len(text) < laenge:
			text += random.choice(vokal)
			if len(text) >= laenge:
				break
			text += random.choice(konsonant)
			if len(text) < laenge and random.randint(0,1):
				text += random.choice(konsonant2)
	text = text.capitalize()
	return text


# Datum
def datum():
	text = str(random.randint(1,31)) + '.' + str(random.randint(1,12)) + '.' + str(random.randint(1950,2012))
	return text


# Essen generieren
voressen = ['Brat', 'Rühr', 'Back', 'Mager', 'Soja', 'Tofu']

def essen(anz):
	if anz:
		if random.randint(0,1):
			essen = random.choice(voressen) + random.choice(nahrung).lower()
		else:
			essen = random.choice(geschmack) + random.choice(nahrung).lower()
	else:
		essen = random.choice(geschmack)
	return essen


# Trinken generieren
getraenk = ['Wasser', 'Saft', 'Tee', 'Kaffee', 'Eistee', 'Milch', 'Sirup', 'Essenz', 'Bier', 'Likör',  'Wein', 'Schnaps']

def trinken():
	trinken = random.choice(geschmack) + random.choice(getraenk).lower()
	return trinken


# Stadt
def stadt():
	if random.randint(0,2):
		stadt = random.choice(stadte).split(' (', 1)
		stadt = stadt[0]
	else:
		stadt = random.choice(stadte)
	return stadt


# Band
gruppe = ['Menschen', 'Personen', 'Tiere', 'Gedärme', 'Kadaver', 'Nudeln', 'Unterhosen', 'Würstchen', 'Bäume', 'Stühle', 'Schweine', 'Neger', 'Alkoholiker', 'Leichen']

def band():
	z = random.randint(0,5)
	if z == 0:
		band = 'Die ' + random.choice(adj).capitalize() + 'en ' + random.choice(gruppe)
	if z == 1:
		band = random.choice(geschmack) + ' ' + random.choice(ort)
	if z == 2:
		band = random.choice(adj).capitalize() + ' ' + random.choice(ort)
	if z == 3:
		band = random.choice(adj).capitalize() + 'e ' + random.choice(nahrung)
	if z == 4:
		band = random.choice(adj).capitalize()
	if z == 5:
		band = wort()
	return band


# Bandart
def bandart():
	if random.randint(0,2):
		m = random.choice(musik)
		if ' ' in m:
			text = m + ' Band'
		elif '-' in m:
			text = m + '-Band'
		else:
			text = m + 'band'
	else:
		text = random.choice(['Band', 'Musikergruppe'])
	return text


# Firma


# Satz generieren

besetzung = ['Sänger', 'Gitarrist', 'Keyboarder', 'Bassist', 'Schlagzeuger', 'Manager', 'Geiger', 'Trompeter', 'Saxophonist', 'Backgroundsänger']

def satz():
	z = 11#random.randint(0,9)
	if z == 0: # Standardsatz mit getrenntem Verb
		v1, v2 = random.choice(verb2).split(",")
		satz = person() + ' ' + v1 + ' ' + random.choice(adj) + ' ' + random.choice(ort) + ' ' + v2
		if random.randint(0,5) == 1: # Chance 1/6
			satz += random.choice(ns)
		satz += '.'
	if z == 1: # Standardsatz
		satz = person() + ' ' + random.choice(verb) + ' ' + random.choice(adj) + ' ' + random.choice(ort)
		if random.randint(0,5) == 1: # Chance 1/6
			satz += random.choice(ns)
		satz += '.'
	if z == 2: # Essen
		satz = person() + ' isst'
		x = random.randint(0,8)
		if x == 1:
			satz += ' gerade'
		elif x == 2:
			satz += ' gerne'
		elif x == 3:
			satz += ' nicht gerne'
		elif x == 4:
			satz += ' oft'
		elif x == 5:
			satz += ' selten'
		satz += ' ' + essen(random.randint(0,2))
		if random.randint(0,3) == 3:
			satz += ' mit ' + essen(random.randint(0,2))
		satz += '.'
	if z == 3: # Trinken
		satz = person() + ' trinkt'
		x = random.randint(0,10)
		if x == 1:
			satz += ' gerade'
		elif x == 2:
			satz += ' gerne'
		elif x == 3:
			satz += ' nicht gerne'
		elif x == 4:
			satz += ' oft'
		elif x == 5:
			satz += ' selten'
		elif x == 6:
			satz += ' jeden Abend ein Glas'
		satz += ' ' + trinken() + '.'
	if z == 4: # Essen und Trinken
		satz = person() + ' isst ' + essen(random.randint(0,2)) + ' und trinkt ' + trinken() + '.'
	if z == 5: # Essen oder Trinken am Ort
		satz = person()
		if random.randint(0,1):
			satz += ' ist '
		else:
			satz += ' sitzt '
		satz += random.choice(ort) + ' und '
		if random.randint(0,1):
			satz += 'isst ' + essen(random.randint(0,2))
		else:
			satz += 'trinkt ' + trinken()
		satz += '.'
	if z == 6: # Bandmitglied
		if random.randint(0,1): # männlich
			satz = random.choice(vornamen_m) + e5(' ' + random.choice(nachnamen)) + ' ist ' + e5('der ') + random.choice(besetzung) + e5(' von') + ' der ' + bandart() + ' "' + band() + '".'
		else: # weiblich
			satz = random.choice(vornamen_w) + e5(' ' + random.choice(nachnamen)) + ' ist ' + e5('die ') + random.choice(besetzung) + 'in' + e5(' von') + ' der ' + bandart() + ' "' + band() + '".'
	if z == 7: # Band gegründet
		if random.randint(0,1):
			satz = 'Die ' + bandart() + ' ' + band() + ' wurde'
		else:
			satz = band() + ' (' + bandart() + ') wurde'
		if random.randint(0,1): # 50% Datum oder Jahr
			satz += ' am ' + datum()
		else:
			if random.randint(0,1):
				satz += ' ' + random.choice(['Anfang', 'Mitte', 'Mitte des Jahres', 'Ende', 'im Frühling', 'im Sommer', 'im Herbst', 'im Winter'])
			satz += ' ' + str(random.randint(1950, 2012))
		if random.randint(0,1): # 50% Ort
			satz += ' in ' + stadt()
		satz += ' gegründet.'
	if z == 8: # Bandmitglieder mit Nachnamen
		satz = 'Die '+ bandart() + ' "' + band() + '" besteht aus ' + random.choice(vornamen) + ' ' + random.choice(nachnamen)
		for i in range(0,random.randint(0,6)): # 2 bis 8 Mitglieder
			satz += ', ' + random.choice(vornamen) + ' ' + random.choice(nachnamen)
		satz += ' und ' + random.choice(vornamen) + ' ' + random.choice(nachnamen) + '.'
	if z == 9: # Bandmitglieder nur mit Vorname
		satz = 'Die '+ bandart() + ' "' + band() + '" besteht aus ' + random.choice(vornamen)
		for i in range(0,random.randint(0,6)): # 2 bis 8 Mitglieder
			satz += ', ' + random.choice(vornamen)
		satz += ' und ' + random.choice(vornamen) + '.'
	if z == 10: # Arbeiter
		if random.randint(0,1): # männlich
			satz = random.choice(vornamen_m) + ' ist ' + e5('ein ') + random.choice(beruf)
		else: # weiblich
			satz = random.choice(vornamen_w) + ' ist ' + e5('eine ') + random.choice(beruf) + 'in'
			satz = satz.replace('mannin', 'frau') # Restaurantfachmannin => Restaurantfachfrau
			satz = satz.replace('fachkraftin', 'fachkraft')
		satz += '.'
		# bei firma()
	if z == 11: # X ist beruflich
		if random.randint(0,1): # männlich
			satz = random.choice(vornamen_m) + e5(' ' + random.choice(nachnamen))
			if random.randint(0,1): # 50% Beruf anzeigen
				if random.randint(0,1):
					satz += ', der ' + random.choice(beruf) + ','
				else:
					satz += ' (' + random.choice(beruf) + ')'
		else: # weiblich
			satz = random.choice(vornamen_w) + e5(' ' + random.choice(nachnamen))
			if random.randint(0,1): # 50% Beruf anzeigen
				if random.randint(0,1):
					satz += ', die ' + random.choice(beruf) + 'in,'
				else:
					satz += ' (' + random.choice(beruf) + 'in)'
				satz = satz.replace('mannin', 'frau') # Restaurantfachmannin => Restaurantfachfrau
				satz = satz.replace('fachkraftin', 'fachkraft')
		satz += ' ist' + e5(' gerade') + ' beruflich ' + random.choice(ort)
		if not random.randint(0,3):
			satz += random.choice([', das darf der Chef aber nicht wissen', ', hat aber keine Lust mehr und will nach Hause', ' und hat Gummistiefel an', ' und lacht darüber', ' und ist das schrecklich peinlich', ' und setzt sich erstmal', ' und wird dafür ausgelacht', ' und ist glücklich', ' und hat sein Spaß dabei', ' und verliert die Hose'])
		satz += '.'
	return satz

#if random.randint(0,1) #50%
# EOF