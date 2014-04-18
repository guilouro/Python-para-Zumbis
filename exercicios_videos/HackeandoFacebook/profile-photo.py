#!usr/bin/env python 
# -*- coding: utf-8 -*-

from urllib2 import urlopen

user = 'guilherme.louro.3'
url = 'https://graph.facebook.com/'+user+'/picture?type=large'
figura = urlopen(url).read()

arquivo = user+'.jpg'
f = open(arquivo, 'wb')
f.write(figura)
f.close()

print '\'%s\' gravado com sucesso ' %arquivo