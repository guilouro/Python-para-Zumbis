#!usr/bin/env python 
# -*- coding: utf-8 -*-


from urllib2 import urlopen
import json
import access_token

def gravar(amigo):
	size = '/picture?width=200&height=200'
	url = 'https://graph.facebook.com/'+amigo['id'] + size
	figura = urlopen(url).read()

	f = open('FriendsPhotos/'+amigo['name']+'.jpg', 'wb')
	f.write(figura)
	f.close()
	print '%s salvo' %amigo['name']
	

url = 'https://graph.facebook.com/me/friends?access_token='+access_token.token
resp = urlopen(url).read()
data = json.loads(resp.decode('utf-8'))

for amigo in data['data']:
	gravar(amigo)