#!usr/bin/env python
# -*- coding: utf-8 -*-

def parse_bin(n, k):
	lista = []

	for i in range((2**n-1)+1):
		lista.append(bin(i));
		
	lista = sorted(lista, key=lambda x: -x.count('1'))
	return (lista, lista[k-1])

print ("="*150)
print ("Lista:%s \nk-ésimo elemento: %s\n" %(parse_bin(3, 5)))
print ("Lista:%s \nk-ésimo elemento: %s\n" %(parse_bin(4, 10)))
print ("Lista:%s \nk-ésimo elemento: %s\n" %(parse_bin(5, 15)))
print ("="*150)
