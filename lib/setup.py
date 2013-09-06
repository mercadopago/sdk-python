import os
from setuptools import setup

setup(
    name='mercadopago',
    version='0.2.0',
    author='Horacio Casatti <horacio.casatti@mercadolibre.com>',
    author_email='horacio.casatti@mercadolibre.com',
    keywords='api mercadopago checkout payment ipn sdk integration',
    packages=['mercadopago'],
    url='https://github.com/mercadopago/sdk-python.git',
    description='Mercadopago SDK module for Payments integration',
    long_description=open('README.rst').read(),
    install_requires='requests>=1.0.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: Freely Distributable',
    ]
)
