#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Faça um Programa que leia três números e mostre o maior deles.
"""

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

maior = n1

if maior < n2:
	maior = n2

if maior < n3: 
	maior = n3

print ('O maior número é %d' %maior)
