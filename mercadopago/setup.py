import sys
import os


from setuptools import setup
from distutils.core import Command


setup(
    name="mercadopago",
    #TODO version="2.0.4",
    description="Mercadopago SDK module for Payments integration",
    author="Mercado Pago SDK",
    author_email="mp_sdk@mercadopago.com",
    url="https://github.com/mercadopago/sdk-python",
    license="MIT",
    keywords="api mercadopago checkout payment ipn sdk integration lts",
    packages=["mercadopago"],
    long_description=open("README.rst").read(),
    #TODO tests_require=[
    #    'pytest'
    #],
    #TODO python_requires="!=3.0*",
    #TODO PYTEST cmdclass={"test": PyTest},
    project_urls={
        "Source Code": "https://github.com/mercadopago/sdk-python",
        "Documentation | ES": "https://www.mercadopago.com.br/developers/es/reference/",
        "Documentation | PT-BR": "https://www.mercadopago.com.br/developers/pt/reference/",
        "Documentation | EN": "https://www.mercadopago.com.br/developers/en/reference/",
    },
    classifiers=[
        #TODO "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        #TODO OSI? "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: Freely Distributable",
    ],
)
