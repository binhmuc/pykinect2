#!/usr/bin/env python

from distutils.core import setup, Extension
from distutils.command.build import build
import urllib3
import os

http = urllib3.PoolManager()

URL = 'https://raw.githubusercontent.com/numpy/numpy/master/tools/swig/numpy.i'
if not os.path.isfile('numpy.i'):
  with open('numpy.i', 'w') as f:
    # content = urllib3.urlopen(URL).read()
    response = http.request('GET', url)
    f.write(response)

kinect2_module = Extension('_kinect2',
  include_dirs=['src'],
  sources=['kinect2.i', 'src/kinect2.cc'],
  swig_opts=['-c++', '-Isrc'],
  extra_compile_args=['-std=c++11'],
  libraries=['freenect2'])

setup(name='kinect2',
  version='0.1.0',
  description='Python Kinect2 Wrapper',
  author='Joseph Yu',
  author_email='kiddo831007@gmail.com',
  url='https://github.com/kiddos/pykinect2',
  ext_modules=[kinect2_module],
  py_modules=['kinect2'])
