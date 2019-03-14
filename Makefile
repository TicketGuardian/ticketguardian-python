test_all:
	make tests27
	make tests

# Python3
venv:
	pip3 install --user virtualenv
	python3 -m virtualenv venv

install:
	make venv
	venv/bin/pip3 install .
	venv/bin/pip3 install -r requirements/dev.txt

tests:
	make venv
	make install
	venv/bin/python3 -m pytest

# Python2.7
venv27:
	pip2.7 install --user virtualenv
	python2.7 -m virtualenv venv27

install27:
	make venv27
	venv27/bin/pip2.7 install .
	venv27/bin/pip2.7 install -r requirements/dev.txt

tests27:
	make venv27
	make install27
	venv27/bin/python2.7 -m pytest

# Styling
flake8:
	venv/bin/pip3 install -r requirements/extras/style.txt
	venv/bin/flake8
