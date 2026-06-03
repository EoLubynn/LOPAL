lista = []
def supermercado():
    while True:
        opcao = input("Item do supermercado: ")
        if opcao == "sair":
            break
        lista.append(opcao)
supermercado()