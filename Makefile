install: 
	venv/bin/pip3 install -r requirements.txt
	venv/bin/pip3 install .

venv:
	pip3 install --user virtualenv
	python3 -m virtualenv venv

tests:
	make venv
	make install
	venv/bin/python3 -m pytest

flake8:
	venv/bin/flake8
