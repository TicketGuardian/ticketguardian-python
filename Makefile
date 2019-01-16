install: 
	venv/bin/pip3 install .

dev-install:
	venv/bin/pip3 install .
	venv/bin/pip3 install -r requirements/dev.txt

venv:
	pip3 install --user virtualenv
	python3 -m virtualenv venv

tests:
	make venv
	make dev-install
	venv/bin/python3 -m pytest

flake8:
	venv/bin/pip3 install -r requirements/extras/style.txt
	venv/bin/flake8
