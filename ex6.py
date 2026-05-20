usuario = str(input("Insira seu nome de usuário: "))
password = input("Insira sua senha: ")
if usuario == "admin" and password == "1234":
    print("Acesso permitido!")
else:
    print("Acesso negado!")