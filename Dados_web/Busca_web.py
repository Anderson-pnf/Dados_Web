from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import string
from collections import Counter

url = 'https://www.globo.com/'

def obter_text(url):
    repostas = requests.get(url)
    return repostas.text
    
def contar_palavras(conteudo):
    sopa = BeautifulSoup(conteudo,'html.parser')
    texto = sopa.get_text()
    texto = texto.lower()
    texto = texto.translate(str.maketrans('','',string.punctuation))

    palavras = texto.split()
    contagem = Counter(palavras)
    return contagem

def grafico(contagem):
    palavras_c = contagem.most_common(3)
    palavras, frequencia = zip(*palavras_c)

    plt.figure(figsize=(10,10))
    plt.barh(palavras,frequencia)
    plt.xlabel('Frequencia')
    plt.ylabel('Palavras')
    plt.title('Palavra com mais aparições')
    plt.show()

conteudo = obter_text(url)
contagem_palavras = contar_palavras(conteudo)

grafico(contagem_palavras)