#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Indique como um troco deve ser dado utilizando-se um número mínimo de notas. Seu 
algoritmo deve ler o valor da conta a ser paga e o valor do pagamento efetuado desprezando 
os centavos. Suponha que as notas para troco sejam as de 50, 20, 10, 5, 2 e 1 reais, e que 
nenhuma delas esteja em falta no caixa. 
"""
valor = float(input('Entre com o valor: '))
notas = [50,20, 10, 5, 2, 1]
i = 0
while valor > 0:
	n = valor/notas[i]
	valor = valor%notas[i]
	if int(n) != 0:
		print('%d notas de R$ %.2f' %(n, notas[i]))
	i += 1