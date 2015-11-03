#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pickle import load

__author__ = 'Luciferz2012'

for row in load(open('06.txt', 'rb')):
    result = ''
    for chars in row:
        result += chars[0] * chars[1]
    print(result)
