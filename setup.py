#!/usr/bin/env python

# This will try to import setuptools. If not here, it will reach for the embedded
# ez_setup (or the ez_setup package). If none, it fails with a message
try:
    from setuptools import setup
except ImportError:
    try:
        import ez_setup
        ez_setup.use_setuptools()
    except ImportError:
        raise ImportError("Hachoir is a Python library used to represent of "
                          "a binary file as a tree of Python objects. Each "
                          "object has a type, a value, an address, etc. The "
                          "goal is to be able to know the meaning of each bit"
                          " in a file..")

from setuptools import setup, find_packages

exec(open('moviepy/version.py').read()) # loads __version__

setup(name='moviepy',
      version='1.3.3',
      author='Julien Muchembled, Victor Stinner',
      description='Represent binary files as a tree of Python objects',
      long_description=open('README.rst').read(),
      url='https://github.com/eduardoburgoa/hachoir_core',
      license='GNU GPL v2',
      keywords="file binary metadata",
      packages=find_packages(exclude='docs'),
      install_requires=[])
