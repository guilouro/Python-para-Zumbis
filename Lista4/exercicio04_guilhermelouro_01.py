#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar 
as funções max e min. 
"""

import random

lista = []
maior = 0
menor = 100

for i in range(10):
	n = random.randint(1,100)
	lista.append(n)

	if n < menor: 
		menor = n
	if n > maior:
		maior = n

lista.sort()
print "="*40
print lista
print("\nMenor: %d - Maior: %d" %(menor, maior))
print "="*40