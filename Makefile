
default:

wheel:
	python setup.py bdist_wheel

tests:
	pytest
