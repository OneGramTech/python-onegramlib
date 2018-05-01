#!/usr/bin/env python

from setuptools import setup

# Work around mbcs bug in distutils.
# http://bugs.python.org/issue10945
import codecs
try:
    codecs.lookup('mbcs')
except LookupError:
    ascii = codecs.lookup('ascii')
    codecs.register(lambda name, enc=ascii: {True: enc}.get(name == 'mbcs'))

VERSION = '1.0.0'

setup(
    name='onegramlib',
    version=VERSION,
    description='Python library for onegram-based blockchains',
    long_description=open('README.md').read(),
	download_url='https://https://gitlab.com/onegram-developers/python-onegramlib/-/archive/' + VERSION + '/python-onegramlib-' + VERSION + '.zip',
    author='Frantisek Horvath',
    author_email='frantisek.horvath@01cryptohouse.com',
    maintainer='Frantisek Horvath',
    maintainer_email='frantisek.horvath@01cryptohouse.com',
    url='https://gitlab.com/onegram-developers/python-onegramlib',
    keywords=[
        'onegram',
        'api',
        'rpc',
        'ecdsa',
        'secp256k1'
    ],
    packages=["onegramapi",
              "onegrambase",
              ],
    install_requires=["ecdsa",
                      "requests",
                      "websocket-client",
                      "pylibscrypt",
                      "pycryptodome",
                      ],
    classifiers=['License :: OSI Approved :: MIT License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 3',
                 'Development Status :: 3 - Alpha',
                 'Intended Audience :: Developers',
                 ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    include_package_data=True,
)
