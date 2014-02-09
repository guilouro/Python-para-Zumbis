#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Determine se um ano é bissexto. Verifique no Google como fazer isso...
"""

ano = str(input("Entre com um ano: "))

if int(ano) % 4 == 0 and ano[2:] != '00':
	print ("%s é um ano bissexto" %ano)
else:
	print ("%s não é um ano bissexto" %ano)

