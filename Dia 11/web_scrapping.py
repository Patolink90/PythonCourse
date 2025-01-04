import bs4
import requests

resultado = requests.get("https://escueladirecta-blog.blogspot.com/2024/07/buscas-trabajo-y-no-has-certificado-en.html")

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
sopa_dos = bs4.BeautifulSoup(resultado.text, 'lxml')
#print(sopa.select('title'))
#print(sopa.select('title')[0])
#print(sopa_dos.select('h1')[0].getText())

parrafo_especial = sopa.select('p')[13].getText()
#print(parrafo_especial)

columna_lateral = sopa.select('.post-title')
#print(columna_lateral)

for elemento in columna_lateral:
    print(elemento.getText())

