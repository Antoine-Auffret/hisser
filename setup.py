import os
from setuptools import setup, find_packages
from setuptools.extension import Extension

import hisser

extensions = [Extension('hisser.pack', ['hisser/pack.c']),
              Extension('hisser.jsonpoints', ['hisser/jsonpoints.cpp'])]

setup(
    name='hisser',
    version=hisser.version,
    url='https://github.com/baverman/hisser',
    author='Anton Bobrov',
    author_email='baverman@gmail.com',
    license='MIT',
    description='Fast TSDB backend for graphite',
    long_description=open('README.rst').read(),
    packages=find_packages(exclude=['tests']),
    install_requires=['msgpack', 'click', 'lmdb', 'xxhash', 'covador', 'nanoio'],
    ext_modules=extensions,
    entry_points={
        'console_scripts': ['hisser = hisser.__main__:cli']
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
