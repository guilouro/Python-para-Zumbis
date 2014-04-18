#!usr/bin/env python 
# -*- coding: utf-8 -*-

from urllib2 import urlopen
import json
import access_token

url = 'https://graph.facebook.com/me/friends?access_token='+access_token.token
resp = urlopen(url).read()
data = json.loads(resp.decode('utf-8'))

for amigo in data['data']:
	print "%s - ID: (%s)" %(amigo['name'], amigo['id'])