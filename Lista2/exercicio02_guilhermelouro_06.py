#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule
e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% \para o Imposto de Renda,
8% \para o INSS e 5% \para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS,
quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os
descontos e o salário líquido, conforme a tabela abaixo:
a. + Salário Bruto : R$
b. - IR (11%) : R$
c. - INSS (8%) : R$
d. - Sindicato ( 5%) : R$
e. = Salário Liquido : R$

"""

qnt_ganha = float(input('Quanto ganha por hora? '))
horas_trabalhadas = int(input('Horas trabalhadas por mês: '))

salario_bruto = qnt_ganha * horas_trabalhadas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

print ('+ Salário Bruto : R$ %.2f' %salario_bruto)
print ('- IR: R$ %.2f' %ir )
print ('- INSS: R$ %.2f' %inss )
print ('- Sindicato: R$ %.2f' %sindicato )
print ('= Salário Liquido : R$ %.2f' %(salario_bruto - ir - inss - sindicato))
