#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a 
quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante 
perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o 
total de dias. 
"""

qntCigarros = int(input("Qnts cigarros por dia: "))
anosFumando = int(input("Anos fumando: "))

totalCigarros = (anosFumando * 365)*qntCigarros
diasPerdidos = (totalCigarros * 10)/24

print ('Dias perdidos %d' %diasPerdidos )