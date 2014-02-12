#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Dizemos que um número natural é triangular se ele é produto de três números naturais 
consecutivos. Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n, 
verificar se n é triangular. 
"""
n1 = int(input('Entre com o número: '))
i = 1
t = 0
while t < n1:
	t = i*(i+1)*(i+2)
	i += 1

if t == n1:
	print ('%d é triangular' %n1)
else: 
	print ('%d não é triangular' %n1)
