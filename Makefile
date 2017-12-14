
default:

wheel:
	python setup.py bdist_wheel

test:
	pytest

upload:
	python setup.py sdist upload --sign
