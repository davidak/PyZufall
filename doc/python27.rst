Python 2.7 Kompatibilität
=========================

PyZufall wird für Python 3 entwickelt.

Es funktioniert auch mit Python 2.7, wird sogar produktiv eingesetzt.

Allerdings laufen die Doctests nicht fehlerfrei durch. Das liegt an Encoding-Problemen, die durch Python 3 behoben wurden und nicht zurückportiert werden. Siehe `#1293741 <http://bugs.python.org/issue1293741>`_.

Da die Tests immer fehlschlagen werden, wird gegen Python 2.7 nicht mehr automatisch getestet.

Du kannst sie aber mit folgendem Befehl selber ausführen::

	$ python2.7 test.py
	Doctest: pyzufall.generator.adjektiv ... ok
	Doctest: pyzufall.generator.band ... ok
	Doctest: pyzufall.generator.bandart ... ok
	Doctest: pyzufall.generator.baum ... ok
	Doctest: pyzufall.generator.beilage ... ok
	Doctest: pyzufall.generator.beruf_m ... ok
	Doctest: pyzufall.generator.beruf_w ... ok
	Doctest: pyzufall.generator.color ... ok
	Doctest: pyzufall.generator.datum ... ok
	Doctest: pyzufall.generator.email ... ok
	Doctest: pyzufall.generator.essen ... ok
	Doctest: pyzufall.generator.farbe ... ok
	Doctest: pyzufall.generator.geburtsdatum ... ok
	Doctest: pyzufall.generator.gegenstand ... ok
	Doctest: pyzufall.generator.geschlecht ... ok
	Doctest: pyzufall.generator.interesse ... ok
	Doctest: pyzufall.generator.koerperteil ... ok
	Doctest: pyzufall.generator.nachname ... ok
	Doctest: pyzufall.generator.ort ... ok
	Doctest: pyzufall.generator.person_m ... ok
	Doctest: pyzufall.generator.person_objekt_m ... ok
	Doctest: pyzufall.generator.person_objekt_w ... ok
	Doctest: pyzufall.generator.person_w ... ok
	Doctest: pyzufall.generator.pflanze ... ok
	Doctest: pyzufall.generator.sprichwort ... ok
	Doctest: pyzufall.generator.stadt ... ok
	Doctest: pyzufall.generator.stadt_bl ... ok
	Doctest: pyzufall.generator.tier ... ok
	Doctest: pyzufall.generator.trinken ... ok
	Doctest: pyzufall.generator.url ... ok
	Doctest: pyzufall.generator.verbd ... ok
	Doctest: pyzufall.generator.verbi ... ok
	Doctest: pyzufall.generator.verbi2 ... ok
	Doctest: pyzufall.generator.verbn ... ok
	Doctest: pyzufall.generator.verbt ... ok
	Doctest: pyzufall.generator.verbt2 ... ok
	Doctest: pyzufall.generator.vorname_m ... ok
	Doctest: pyzufall.generator.vorname_w ... ok
	Doctest: pyzufall.generator.wort ... ok
	Doctest: pyzufall.generator.zahl ... ok
	Doctest: pyzufall.generator.zeitpunkt ... ok
	Doctest: pyzufall.helfer.alter ... ok
	Doctest: pyzufall.helfer.aufzaehlung ... FAIL
	Doctest: pyzufall.helfer.erste_gross ... FAIL
	Doctest: pyzufall.helfer.lese ... ok
	Doctest: pyzufall.helfer.str_add ... FAIL
	Doctest: pyzufall.helfer.uml ... ok
	test.test_satz ... ok
	test.test_satz_frage ... ok
	test.test_sprichwort ... ok

	======================================================================
	FAIL: Doctest: pyzufall.helfer.aufzaehlung
	----------------------------------------------------------------------
	Traceback (most recent call last):
	  File "/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/doctest.py", line 2226, in runTest
	    raise self.failureException(self.format_failure(new.getvalue()))
	AssertionError: Failed doctest test for pyzufall.helfer.aufzaehlung
	  File "/Users/davidak/Sync/code/PyZufall/pyzufall/helfer.py", line 123, in aufzaehlung

	----------------------------------------------------------------------
	File "/Users/davidak/Sync/code/PyZufall/pyzufall/helfer.py", line 136, in pyzufall.helfer.aufzaehlung
	Failed example:
	    aufzaehlung(b)
	Expected:
	    'Überwachen und Strafen'
	Got:
	    '\xc3\x9cberwachen und Strafen'


	======================================================================
	FAIL: Doctest: pyzufall.helfer.erste_gross
	----------------------------------------------------------------------
	Traceback (most recent call last):
	  File "/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/doctest.py", line 2226, in runTest
	    raise self.failureException(self.format_failure(new.getvalue()))
	AssertionError: Failed doctest test for pyzufall.helfer.erste_gross
	  File "/Users/davidak/Sync/code/PyZufall/pyzufall/helfer.py", line 63, in erste_gross

	----------------------------------------------------------------------
	File "/Users/davidak/Sync/code/PyZufall/pyzufall/helfer.py", line 72, in pyzufall.helfer.erste_gross
	Failed example:
	    erste_gross('über Stock und Stein.')
	Expected:
	    'Über Stock und Stein.'
	Got:
	    '\xc3\xbcber Stock und Stein.'
	----------------------------------------------------------------------
	File "/Users/davidak/Sync/code/PyZufall/pyzufall/helfer.py", line 75, in pyzufall.helfer.erste_gross
	Failed example:
	    erste_gross('älter als das Internet!')
	Expected:
	    'Älter als das Internet!'
	Got:
	    '\xc3\xa4lter als das Internet!'


	======================================================================
	FAIL: Doctest: pyzufall.helfer.str_add
	----------------------------------------------------------------------
	Traceback (most recent call last):
	  File "/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/doctest.py", line 2226, in runTest
	    raise self.failureException(self.format_failure(new.getvalue()))
	AssertionError: Failed doctest test for pyzufall.helfer.str_add
	  File "/Users/davidak/Sync/code/PyZufall/pyzufall/helfer.py", line 81, in str_add

	----------------------------------------------------------------------
	File "/Users/davidak/Sync/code/PyZufall/pyzufall/helfer.py", line 93, in pyzufall.helfer.str_add
	Failed example:
	    str_add('blöd', 'e')
	Expected:
	    'blöde'
	Got:
	    'bl\xc3\xb6de'


	----------------------------------------------------------------------
	Ran 50 tests in 1.290s

	FAILED (failures=3)
