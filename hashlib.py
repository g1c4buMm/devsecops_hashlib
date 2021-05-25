# Python Script - Validação de usuário com hashlib e getpass
# Importando módulos de Segurança:
from getpass import getpass
import hashlib
#
# Criação de lista vazia denominada "usuarios"
usuarios = []
usuario = {
    "name": "Clark Kent", 
    "username" : "kent",
    "password" : "6c70795dc50a2d6765a44bceda2699c48a8e81effe3f9e7cf3b6f8bb34ccb5b2"
}
usuarios.append(usuario)
usuario = {
    "name": "Bruce Wayne",
    "username" : "wayne",
    "password" : "0bf3116d14ceeb7b8859abb9f5b90a7747913185930fed774a949cc8777a990a"
}
usuarios.append(usuario)
usuario = {
    "name": "Christopher Walker",
    "username" : "walker",
    "password" : "db7e65b576f6b3db9041cbddff92f9a4b7253b795aab817d3f348977b014cd83"
}
usuarios.append(usuario)
#Solicita a entrada do usuário, salvando em uma variável "user"
user=str(input("Enter username: "))
#Solicita a entrada da senha, convertendo-a para byte seguido da criptografia para sha256 logo em seguida
password=hashlib.sha256(getpass("Enter password: ").encode())
#Conta a quantidade de usuario na lista usuarios
numuser=len(usuarios)
#Contador para validação do usuário correto
count=0
#Contador para validar encerrar loop "for" para apresentar mensagem de usuário incorreto:
error=0
#validação do usuário e senha
for reg in usuarios:
    if user == (reg["username"]):
        count=count+1
        if count>0:
            if user == (reg["username"]) and (password.hexdigest()) == (reg["password"]):
                print (reg["name"], "logado")
            else: print("Usuário/senha inválidos")
    else: error=error+1
    if error == numuser:
        print("Usuário/senha inválidos")
        break
