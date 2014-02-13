#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Verifique se um inteiro positivo n é primo.
"""
n = int(input('Entre com o número: '))
i = 1
divisor = 0

while i <= n:
	if (n%i) == 0:
		divisor += 1
	i += 1

if divisor == 2:
	print ("%d é primo" %n)
else:
	print ("%d não é primo" %n)