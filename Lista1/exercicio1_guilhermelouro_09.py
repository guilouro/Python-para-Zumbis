#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo 
usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, 
sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado. 
"""
kmp = int(input("Digite a quantidade de km percorridos: "))
dias = int(input("Digite a quantidade de dias: "))

print ('Valor do aluguel: R$ %.2f' %(kmp*0.15 + dias*60) )