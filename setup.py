# -*- coding: utf-8 -*-
"""
sequoia-calculator.
-----
It is a package of a calculator to realize observation time
-----
And Easy to Setup
`````````````````
And run it:
.. code:: bash
    $ pip install git+https://github.com/ryszard-ps/sequoia-calculator.git
  <https://github.com/Ryszard-Ps/sequoia-calculator.git>`_
"""

from codecs import open
from os import path

from sequoia_calculator.version import version
from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='sequoia_calculator',
    version=version,
    description='SEQUOIA Integration Time Calculator',
    long_description=long_description,
    url='https://github.com/Ryszard-Ps/sequoia-calculator.git',
    author='Ricardo Pascual',
    author_email='hello@rjbits.com',
    license='GPLv3',
    classifiers=[
        'Development Status ::  5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public Licence v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries'
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords='calculator sequoia hedwig',
    packages=find_packages(exclude=['docs', 'tests']),
)
