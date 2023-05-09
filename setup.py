#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 11:07:23 2023

@author: matthewbattley
"""

import setuptools

setuptools.setup(
    name="rv_curve_jura",
    version="0.1",
    author="Matthew Battley",
    author_email ="matbatt@gmail.com",
    description="Plot all RV curves that you want",
    packages=setuptools.find_packages(),
    install_requires = ["numpy","matplotlib"],
    classifiers=["Programming language :: Python :: 3"],
    )