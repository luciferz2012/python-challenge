#!/usr/bin/env python
# -*- coding: utf-8 -*-
from zipfile import ZipFile

__author__ = 'Luciferz2012'

file = ZipFile('channel.zip')
hint = 'Next nothing is'
nothing = 90052
result = ''
while True:
    filename = '{nothing}.txt'.format(nothing=nothing)
    content = file.read(filename).decode()
    result += file.getinfo(filename).comment.decode()
    print(content)
    if not content.startswith(hint):
        break
    nothing = content.split()[-1]
print(result)
