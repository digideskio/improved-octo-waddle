# ----------------------------------------------------------------------------
# Copyright (c) 2013--, BP development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------
import os
from setuptools import setup
from setuptools.extension import Extension

import numpy as np

classes = """
    Development Status :: 4 - Beta
    License :: OSI Approved :: BSD License
    Topic :: Scientific/Engineering
    Programming Language :: Python
    Programming Language :: Python :: 3.4
    Programming Language :: Python :: 3.5
    Operating System :: Unix
    Operating System :: POSIX
    Operating System :: MacOS :: MacOS X
"""
classifiers = [s.strip() for s in classes.split('\n') if s]

long_description = """An implementation of a balanced tree as described by
Cordova and Navarro"""

from Cython.Compiler.Options import directive_defaults

#directive_defaults['linetrace'] = True
#directive_defaults['binding'] = True

USE_CYTHON = os.environ.get('USE_CYTHON', True)
ext = '.pyx' if USE_CYTHON else '.c'
extensions = [Extension("bp._bp",
                        ["bp/_bp" + ext], ),
              Extension("bp._io",
                        ["bp/_io" + ext], ),
              Extension("bp._conv",
                        ["bp/_conv" + ext], ),
              Extension("bp._binary_tree",
                        ["bp/_binary_tree" + ext], ),
              Extension("bp.tests.test_bp_cy",
                        ["bp/tests/test_bp_cy" + ext])]

extensions.extend([Extension("bp._ba",
                            ["bp/_ba" + ext], include_dirs=['BitArray/'],
                             library_dirs=['BitArray/'],
                             libraries=['bitarr'])])


if USE_CYTHON:
    from Cython.Build import cythonize
    extensions = cythonize(extensions)#, compiler_directives={'CYTHON_TRACE':1})
setup(name='bp',
      version=0.1,
      description='Balanced parentheses',
      author='Daniel McDonald',
      author_email='mcdonadt@colorado.edu',
      maintainer='Daniel McDonald',
      maintainer_email='mcdonadt@colorado.edu',
      url='https://github.com/wasade/improved-octo-waddle',
      packages=['bp'],
      ext_modules=extensions,
      include_dirs=[np.get_include()],
      setup_requires=['numpy >= 1.9.2'],
      install_requires=[
          'numpy >= 1.9.2',
          'nose >= 1.3.7',
          'cython >= 0.24.1'],
      long_description=long_description)
