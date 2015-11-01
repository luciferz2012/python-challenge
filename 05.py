#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib.request import urlopen

__author__ = 'Luciferz2012'


def test(nothing):
    return urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s' % nothing).read().decode('utf-8')


hint = 'and the next nothing is'
# nothing = 12345
# nothing = 94485
# nothing = 16044 / 2
nothing = 63579
while True:
    content = test(nothing)
    print(content)
    if not content.startswith(hint):
        break
    nothing = content.split()[-1]
