install: 
	pip3 install -r requirements.txt
	pip3 install .

venv:
	pip3 install --user virtualenv
	python3 -m virtualenv venv

tests:
	make sdk
	python3 -m pytest
