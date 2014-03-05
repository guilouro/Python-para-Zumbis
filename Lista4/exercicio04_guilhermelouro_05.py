#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Seja o statement sobre diversidade: “The Python Software Foundation and the global Python 
community welcome and encourage participation by everyone. Our community is based on 
mutual respect, tolerance, and encouragement, and we are working to help each other live up 
to these principles. We want our community to be more diverse: whoever you are, and 
whatever your background, we welcome you.”

Seja o mesmo texto acima “splitado”. Calcule quantas palavras possuem uma das letras 
“python” e que tenham mais de 4 caracteres. Não se esqueça de transformar maiúsculas para 
minúsculas e de remover antes os caracteres especiais. 

"""

texto = "The Python Software Foundation and the global Python \
community welcome and encourage participation by everyone. Our community is based on \
mutual respect, tolerance, and encouragement, and we are working to help each other live up \
to these principles. We want our community to be more diverse: whoever you are, and \
whatever your background, we welcome you."

texto = texto.translate(None, ',.')
palavras = texto.split()
in_python = []
maior_q_4 = 0

for s in palavras:
	p = s.lower()
	if p[0] in "python":
		in_python.append(s);
		if(len(s) > 4): 
			maior_q_4 += 1


print "\n\n", "="*80
print ("%d palavras possuem uma das letras de 'python' e tem mais de 4 caracteres." %maior_q_4)
print "="*80, "\n\n"