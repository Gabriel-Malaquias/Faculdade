import json
import cadastro
import conversao

arquivo = "dados.json"

def carregar_json():
  with open(arquivo, "r", encoding="UTF-8") as file:
    return json.load(file)

def logar():
  dados = carregar_json()

  while(True):
    print("===============")
    usuario = str(input("Usuário: "))
    senha = str(input("Senha: "))
    print("===============")

    login = False

    for informacao in dados:
      if(usuario == informacao['nome'] and senha ==     informacao['senha']):
        login = True
        print("Login Realizado")
        conversao.converter_moeda()
        
    if login:
      break
    else:
      resp = str(input("Erro de Credenciais ! Deseja Continuar [S/N]")).upper()
      if(resp == "SIM" or resp == "S"):
        cadastro.cadastrar()
        dados = carregar_json()
      else:
        break

logar()