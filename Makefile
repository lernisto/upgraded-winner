clean:
	rm -rf build dist *.egg-info

dist: clean
	python setup.py bdist_wheel

install: dist
	pip install -U dist/*

requirements.txt: Pipfile
	pipenv lock -r >requirements.txt

dev-requirements.txt: Pipfile
	pipenv lock --dev -r >dev-requirements.txt

test: test requirements.txt dev-requirements.txt
	tox

.PHONY: clean dist install test
