#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 6) Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

dist = float(input("Digite a distancia em Km: "))
velo = float(input("Digite a velocidade média: "))

tempo = dist / velo

print ('Tempo em horas %.1f' %tempo)