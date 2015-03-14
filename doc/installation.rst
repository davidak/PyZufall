Installation
============

Mit der Paketverwaltung `pip <http://www.pip-installer.org/en/latest/>`_ lassen sich Python-Pakete vom `Python Package Index <https://pypi.python.org/pypi/vcardgen/>`_ (PyPI) herunterladen und installieren.

Die neuste stabile Version von **PyZufall** installierst du mit::

	# pip install pyzufall

.. hint::

	Auf älteren Systemen ruft der Befehl pip für Python 2.x auf. PyZufall wird für Python 3 entwickelt. Wenn du PyZufall mit Python 2.x einsetzen willst, beachte die Seite :doc:`python27`.

Pip für **Python 3** wird auf vielen System (z.B OS X oder Ubuntu) wie folgt ausgeführt::

	# pip-3.2 install pyzufall

.. hint::

	Pip benötigt root-Rechte für die Installation neuer Pakete. Wenn du nicht root bist benutze sudo.

Oder du installierst **PyZufall** manuell, indem du die neuste Version vom `PyPI <https://pypi.python.org/pypi/pyzufall>`_ runterlädst, diese entpackst und installierst.
::
	
	# wget https://pypi.python.org/packages/source/P/PyZufall/PyZufall-0.11.tar.gz
	# tar -xzf PyZufall-0.11.tar.gz
	# cd PyZufall-0.11/
	# python3 setup.py install
