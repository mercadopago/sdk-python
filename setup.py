"""
    Module: setup.py
"""

import unittest
from setuptools import setup


setup(
    name="mercadopago",
    version="2.0.0",
    description="Mercadopago SDK module for Payments integration",
    author="Mercado Pago SDK",
    author_email="mp_sdk@mercadopago.com",
    url="https://github.com/mercadopago/sdk-python",
    license="MIT",
    keywords="api mercadopago checkout payment in sdk integration lts",
    packages=["mercadopago"],
    long_description=open("README.md").read(),
    tests_require=[
        "unittest"
    ],
    python_requires="!=3.0*",
    cmdclass={"test": unittest},
    project_urls={
        "Source Code": "https://github.com/mercadopago/sdk-python",
        "Documentation | EN": "https://www.mercadopago.com.br/developers/en/reference/",
        "Documentation | ES": "https://www.mercadopago.com.br/developers/es/reference/",
        "Documentation | PT-BR": "https://www.mercadopago.com.br/developers/pt/reference/",
    },
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: Freely Distributable",
    ],
)
