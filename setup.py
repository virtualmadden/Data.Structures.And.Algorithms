#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from setuptools import setup

about = {}
with open("src/__about__.py") as f:
    exec(f.read(), about)

setup(
    name=about['__title__'],
    version=about['__version__'],
    url=about['__url__'],
    license=about['__license__'],
    author=about['__author__'],
    description=about['__description__'],
    long_description=__doc__,
    packages=['src'],
    zip_safe=False,
    platforms='any',
    install_requires=['PyTest'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development',
    ]
)
