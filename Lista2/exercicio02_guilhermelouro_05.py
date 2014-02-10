#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Faça um Programa que leia três números e mostre o maior e o menor deles.
"""

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

maior = n1
menor = n1

if maior < n2:
	maior = n2

if maior < n3: 
	maior = n3

if menor > n2:
	menor = n2

if menor > n3:
	menor = n3

print ('Maior:  %d ' %maior)
print ('Menor:  %d ' %menor)
