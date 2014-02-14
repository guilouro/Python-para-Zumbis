#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os 
números ímpares na lista IMPAR. Imprima as três listas. 
"""

import random

lista = []
par = []
impar = []

for i in range(20):
	n = random.randint(1,100)
	lista.append(n)

	if n % 2 == 0: 
		par.append(n)
	else:
		impar.append(n)

lista.sort()
par.sort()
impar.sort()

print "\nLISTA = ", lista
print "PAR   = ", par
print "IMPAR = ", impar, "\n"
