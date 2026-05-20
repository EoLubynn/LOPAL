vendas = []
def menu():
    while True:
        print("===Menu de Vendas===\n1. Registrar Venda;\n2. Listar Vendas;\n3. Sair.\n")
        opcao = input("Selecione uma opção.\n")
        if opcao == "Registrar Venda" or opcao == "registrar venda" or opcao == "1":
            vendas.append(int(input("Receita: R$")))
            print("Venda registrada.\n")
        elif opcao == "Listar Vendas" or opcao == "listar vendas" or opcao == "2":
            print("===Lista de Vendas===")
            melhor = max(vendas)
            menor = min(vendas)
            media = sum(vendas) / len(vendas)
            for venda in vendas:
                print("R$", venda, sep="")
            print("\nMelhor receita: R$", melhor, "\nMenor receita: R$", menor, "\nMédia: R$", media, "\nTotal: R$", sum(vendas), sep="")
            print("")
        elif opcao == "Sair" or opcao == "sair" or opcao == "3":
            print("Encerrando programação...")
            break
menu() 