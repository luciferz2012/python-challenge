#!/usr/bin/env python
# -*- coding: utf-8 -*-
from string import ascii_lowercase

__author__ = 'Luciferz2012'

src = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''

x = ascii_lowercase
y = x[2:] + x[:2]
table = ''.maketrans(x, y)
print(src.translate(table))

url = 'map'

print(url.translate(table))
