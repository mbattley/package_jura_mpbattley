#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 11:07:23 2023

@author: matthewbattley
"""

import setuptools

with open("README.md", 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="rv_curve_jura",
    version="0.1",
    author="Matthew Battley",
    author_email ="matbatt@gmail.com",
    description="Plot all RV curves that you want",
    packages=setuptools.find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/mbattley/package_jura_mpbattley',
    install_requires = ["numpy","matplotlib"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        ],
    )