#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 3) Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.

dias = int(input("Digite uma quantidade de dias: "))
horas = int(input("Digite uma quantidade de horas: "))
minutos = int(input("Digite uma quantidade de minutos: "))
segundos = int(input("Digite uma quantidade de segundos: "))

totalSegundos = (dias*24*60*60) + (horas*60*60) + (minutos*60) + segundos

# print (dias,"dias",horas,"horas",minutos,"minutos",segundos,"segundos representam", totalSegundos,"segundos")
print(f'{dias} dias {horas} horas {minutos} minutos {segundos} segundos representam {totalSegundos} segundos')
