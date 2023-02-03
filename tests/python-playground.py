# -*- coding: utf-8 -*- 
import requests

url = 'http://google.com/favicon.ico'
r = requests.get(url, allow_redirects=True)
with open('google.ico', 'wb') as dl_file:
    write_content = dl_file.write(r.content)








