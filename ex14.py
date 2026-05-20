password = ["12345678", "87654321", "qawsedrf"]
senha = " "
while senha != password:
    senha = input("Digite a senha.\n")
    if senha in password:
        print("Acesso concebido.")
        break
    else:
        print("Acesso negado. Tente mais uma vez.")
