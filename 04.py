#!/usr/bin/env python
# -*- coding: utf-8 -*-
from re import findall

__author__ = 'Luciferz2012'

src = open('04.txt').read()

print(''.join(findall('[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]', src)))
