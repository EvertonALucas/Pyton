import requests
from bs4 import BeautifulSoup
 
pagina = requests.get('http://www.uninove.br')
 
sopa = BeautifulSoup(pagina.text, 'html.parser')
