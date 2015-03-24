# -*- coding: utf-8 -*-

import setuptools

setuptools.setup(
    name='broadcast_glue',
    version='0.1.0',
    url='http://github.com/jkoelker/broadcast_glue',

    author='Jason Kölker',
    author_email='jason@koelker.net',

    description='Glue In-Home Streaming discovery broadcasts between subnets',
    long_description=open('README.rst').read(),

    license='MIT',
    packages=setuptools.find_packages(),

    install_requires=['netaddr', 'netifaces', 'gevent'],
    entry_points={
        'console_scripts': ['broadcast-glue=broadcast_glue.cmd:main']
        },

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
