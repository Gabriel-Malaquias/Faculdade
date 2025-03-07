import requests
import json

def pegar_cotacao(origem, destino):
  link = f"https://economia.awesomeapi.com.br/json/last/{origem}-{destino}"
  dados = requests.get(link)
  cotacao = dados.json()[f'{origem}{destino}']['bid']
  return cotacao

def converter_moeda():
  resp1 = str(input("Moeda de Origem: ")).upper()
  resp2 = str(input("Moeda de Destino: ")).upper()
  valor = float(input("Valor a ser convertido: "))

  taxa = pegar_cotacao(resp1, resp2)
  conversao = float(valor) / float(taxa)
  print(f"O valor {valor} equivale a {conversao:.2f}")
  