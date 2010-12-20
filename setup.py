#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2010 Gora Khargosh <gora.khargosh@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import sys
import imp
import os.path

from setuptools import setup, find_packages

SRC_DIR = 'src'
PKG_DIR = os.path.join(SRC_DIR, 'watchmedo_webtricks')

version = imp.load_source('version',
                          os.path.join(PKG_DIR, 'version.py'))

def read_file(filename):
    """
    Reads the contents of a given file relative to the directory
    containing this file and returns it.

    :param filename:
        The file to open and read contents from.
    """
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

if sys.version_info < (3,):
    extra = {}
else:
    extra = dict(use_2to3=True)

setup(name="watchmedo_webtricks",
      version=version.VERSION_STRING,
      description="Watchmedo WebTricks",
      long_description=read_file('README'),
      author="Gora Khargosh",
      author_email="gora.khargosh@gmail.com",
      license="MIT License",
      url="http://github.com/gorakhargosh/watchmedo-webtricks",
      download_url=\
      "http://watchdog-python.googlecode.com/files/watchmedo_webtricks-%s.tar.gz"\
      % version.VERSION_STRING,
      keywords=' '.join([
                            'python',
                            'filesystem',
                            'monitoring',
                            'monitor',
                            'webtricks',
                            'assets',
                            'minify',
                            'minifier',
                            'web',
                            'css',
                            ]
                        ),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries',
          'Topic :: System :: Monitoring',
          'Topic :: System :: Filesystems',
          'Topic :: Utilities',
          ],
      package_dir={'': SRC_DIR},
      packages=find_packages(SRC_DIR),
      include_package_data=True,
      install_requires=['watchdog'],
      zip_safe=False,
      **extra
      )
