from __future__ import absolute_import, print_function

import io
import os

from setuptools import find_packages, setup


def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8'),
    ) as fp:
        return fp.read()


readme = open('README.md').read()

setup(
    name='citeme',
    version='0.1.0',
    license='Apache Software License',
    author='Berend Weel',
    tests_require=['pytest'],
    install_requires=[
        'bibtexparser==0.6.2'
    ],
    extras_require={
        'test': ['pytest', 'pytest-flake8', 'pytest-cov'],
    },
    author_email='b.weel@esiencecenter.nl',
    description=(
        'Library to easily add citations to your code.'
    ),
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
