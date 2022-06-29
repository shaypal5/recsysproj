"""Setup for the recasino package."""

# !/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


README_RST = ''
with open('README.rst', encoding="utf-8") as f:
    README_RST = f.read()

INSTALL_REQUIRES = [
    'pandas>=0.18.0',  # obviously
]
TEST_REQUIRES = [
    # testing and coverage
    'pytest', 'coverage', 'pytest-cov', 'pytest-ordering',
]


setup(
    name='recasino',
    description="Recomment casino games",
    long_description=README_RST,
    long_description_content_type='text/x-rst',
    author="Shay Palachy",
    author_email="shaypal5@gmail.com",
    version='v0.0.1',
    url='https://github.com/shaypal5/recasino',
    license="MIT",
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    extras_require={
        'test': TEST_REQUIRES
    },
    platforms=['any'],
    keywords='recommendations systems',
)
