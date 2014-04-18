#!usr/bin/env python 
# -*- coding: utf-8 -*-

from urllib2 import urlopen
from pprint import pprint
import json

url = 'https://graph.facebook.com/guilherme.louro.3'
resp = urlopen(url).read()
data = json.loads(resp.decode('utf-8'))
pprint(data)