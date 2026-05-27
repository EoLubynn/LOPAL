def cadastro():
    while True:
        print("===Cadastro===")
        nome = input("Usuário: ")
        email = input("Email: ")
        idade = int(input("Idade: "))
        print("\nComputando dados...\n")
        if len(nome) > 3:
            print("Usuário válido.\n")
        else:
            print("Usuário invalido.")
            print("É necessário que o usuário tenha pelo menos 3 caractéres.\n")
        if email.endswith("@gmail.com"):
            print("Email válido.\n")
        else:
            print("Email invalido.")
            print('É necessário que o email acabe com "@gmail.com".\n')
        if idade >= 18:
          print("Maior de idade.\n")
        else:
            print("Menor de idade.")
            print("É necessário ter mais de 18 anos.\n")
        # ===Finalização===
        if len(nome) > 3 and email.endswith("@gmail.com") and idade >= 18:
            print("Todos os critérios foram realizados.")
            print("===Usuário Registrado===")
            break
        else:
            print("Existem critérios não realizados.")
cadastro()