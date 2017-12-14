#!/usr/bin/env python

from setuptools import setup

setup(
    name='domaincheck',
    version='1.0.0',
    author='Matthias Lohr',
    author_email='matthias@lohr.me',
    description='Domain availability check',
    packages=['domaincheck'],
    install_requires=[
        'dnspython',
        'enum'
    ],
    entry_points={
        'console_scripts': ['domaincheck=domaincheck.__main__:main']
    }
)
