import json

arquivo = "dados.json"

def carregar_json():
  with open(arquivo, "r", encoding="UTF-8") as file:
    return json.load(file)

def salvar_dados(novo_user):
  with open(arquivo, "w", encoding="UTF-8") as file:
    json.dump(novo_user, file, indent=4)

def cadastrar():
  dados = carregar_json()

  while(True):
    print("===============")
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    senha = str(input("Senha: "))
    conf_senha = str(input("Confirmar senha: "))
    print("===============")

    novo_user = {
      "nome": str(nome),
      "idade": int(idade),
      "senha": str(senha)
    }

    if(senha == conf_senha):
      dados.append(novo_user)
      salvar_dados(dados)
      print("Cadastro Realizado !")
      break
    else:
      print("Erro ! As senhas não coincidem. Tente novamente !")