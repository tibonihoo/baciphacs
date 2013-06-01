#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
The setup.py script needed to build a .egg for an easier distribution
and installation.

Requires 'Easy Install' to be installed :)
see there: http://peak.telecommunity.com/DevCenter/EasyInstall#installation-instructions

Then to create a package run:
$ python setup.py bdist_egg

To use the generated .egg file then:
easy_install baciphacs-{baciphacs version}-py{python version}.egg

Automagical stuff:

  - test everything::

      python setup.py test

  - build the packages (sources an egg) and upload all the stuff to pypi::

      python setup.py sdist bdist_egg upload

  - build the documentation
   
      python setup.py build_sphinx
"""

import os
from setuptools import setup

# just in case setup.py is launched from elsewhere than the containing directory
originalDir = os.getcwd()
os.chdir(os.path.dirname(os.path.abspath(__file__)))
try:
	setup(
		name = "baciphacs",
		version = __import__("baciphacs").__version__,
		py_modules = ['baciphacs'],
		
		# the unit tests
		test_suite = "test",
		
		# metadata for upload to PyPI
		author = "Thibauld Nion",
		author_email = "thibauld@tibonihoo.net",
		description = "Bar Charts In Pure HTML And CSS",
		license = "BSD",
		keywords = "bar charts HTML CSS",
		url = "https://github.com/tibonihoo/baciphacs",
		# more details
		long_description = open("README.md").read(),
		classifiers=['Development Status :: 5 - Production/Stable',
                             'Intended Audience :: Developers',
                             'License :: OSI Approved :: BSD License',
                             'Operating System :: OS Independent',
                             'Programming Language :: Python',
                             'Topic :: Software Development :: Libraries :: Python Modules'],
		platforms='All',
		)
	
finally:
  os.chdir(originalDir)
