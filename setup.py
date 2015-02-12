#!/usr/bin/env python

from distutils.core import setup, Extension
import numpy,mpi4py

from setuptools import setup, find_packages

setup(name='waveSolutions',
      version='0.0.1',
      description='Wave modules for analytical  water waves.',
      author='Matt Malej',
      author_email='matt.malej@erdc.dren.mil',
      packages=find_packages('src'),
      package_dir={'':'src'},
      package_data={'':['src/*.py']},
      url='https://github.com/eelcovv/waveSolutions',
      requires=['numpy']
      )
