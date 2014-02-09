#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 5) Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar. 

preco = input("Digite o preço: ")
perc = input("Digite a porcentagem do desconto: ")

novoPreco = preco - ((preco*perc)/100)
desconto = preco - novoPreco

print "Preço com desconto: R$", novoPreco
print "Desconto de: R$", desconto