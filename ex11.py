cadastro = ["Kamilly", "Rian", "Leandro", "Santos", "Kalebe"]
solicitado = str(input("Solicite um usuário. \n"))
if solicitado in cadastro:
    print("Este usuário está cadastrado.")
else:
    print("Este usuário não foi cadastrado.")