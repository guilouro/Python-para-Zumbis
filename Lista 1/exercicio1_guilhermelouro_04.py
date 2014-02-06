#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 4) Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário. 

salario = input("Digite o salário: ")
perc = input("Digite a porcentagem do aumento: ")

novoSalario = salario + ((salario*perc)/100)
aumento = novoSalario - salario

print "Aumento de: R$", aumento
print "Novo salário: R$", novoSalario