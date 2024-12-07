from bs4 import BeautifulSoup

html = '''
<!DOCTYPE html>
<html>
    <head>
        <title> 
teste 
        </title>
    </head>
<body>
    <h1> 
TESTE 
    </h1>
    <p> 
lorem1 
    </p>
    <p> 
lorem2 
    </p>
    <a href = 'https://github.com/anderson-pnf' > 
Link de aplicação web
    </a>
</body>

<html>
'''

sopa = BeautifulSoup(html,'html.parser')
titulo = sopa.title.string
print(titulo)

paragrafo = sopa.h1.string
print(paragrafo)

paragrafo1 = sopa.find_all('p')[1].string
print(paragrafo1)

link = sopa.a['href']
print(link)