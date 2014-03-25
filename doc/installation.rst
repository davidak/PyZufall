Installation
============

Mit `pip <http://www.pip-installer.org/en/latest/installing.html>`_ kannst du die neuste stabile Version von **PyZufall** ganz einfach auf deinem System installieren::

	# pip install pyzufall

.. note::

	Meist ruft der Befehl pip für Python 2.x auf. PyZufall wird hauptsächlich für Python 3 entwickelt, bei einem schnellen Test mit Python 2.6 und 2.7 sind allerdings keine Fehler aufgefallen.

Pip für **Python 3** wird auf vielen System (z.B OS X oder Ubuntu) wie folgt ausgeführt::

	# pip-3.2 install pyzufall

.. note::

	Pip benötigt root-Rechte für die Installation neuer Pakete.

Oder du installierst **PyZufall** manuell, indem du die neuste Version von `PyPI <https://pypi.python.org/pypi/pyzufall>`_ runterlädst, diese entpackst und installierst.
::
	
	# wget https://pypi.python.org/packages/source/P/PyZufall/PyZufall-0.11.tar.gz#md5=dea538382e11cd9b537b3d70f205fdc7
	# tar -xzf PyZufall-0.11.tar.gz
	# cd PyZufall-0.11/
	# python3 setup.py install
