#!/usr/bin/env python
#-*- coding:utf-8 -*-

from urllib2 import urlopen
pagina = urlopen('http://beans.itcarlow.ie/prices-loyalty.html')
texto = pagina.read().decode('utf8')
inicio = texto.find(">$") + 2
fim = inicio + 4
preco = float(texto[inicio:fim])

if preco < 4.74:
	print "Comprar! $%.2f" %preco






