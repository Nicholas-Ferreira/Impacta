# 1900519 - Fernando de Souza Franco
# 1900953 - Nicholas Ferreira
# 1901118 - Lara Angelini Argento
# 1900675 - Lucas Eduardo Ano 
# 1901008 - Leonardo Ferreira

from time import sleep
from random import seed
from random import randint
import sys
import http.client
import urllib.request

seed(1)

chave = 'MGTGIEI9ICL92CJM'
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % chave

while True:
  field1 = randint(0, 100)
  field2 = randint(0, 100)

  url = f"{baseURL}&field1={field1}&field2={field2}"
  conn = urllib.request.urlopen(url)
  print(conn.read())
  print(f"f1 = {field1} | f2 = {field2}")
  conn.close()
  sleep(15)


