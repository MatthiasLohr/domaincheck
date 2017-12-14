
default:

release:
	python setup.py sdist bdist bdist_wheel

test:
	pytest

upload:
	python setup.py sdist upload --sign
