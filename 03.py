#!/usr/bin/env python
# -*- coding: utf-8 -*-
from string import ascii_lowercase

__author__ = 'Luciferz2012'

src = open('03.txt').read()

print(''.join([c for c in src if c in ascii_lowercase]))
