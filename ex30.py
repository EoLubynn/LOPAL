produtos = []
def menu():
    while True:
        print("===Menu===\n1.Cadastrar Produtos;\n2.Listar Produtos;\n3.Buscar Produtos;\n4.Remover Produto;\n5.Salvar em Arquivo;\n6.Ler Arquivo;\n0.Sair.")
        opcao = (input("Digite a opção.\n"))
        if opcao == "1":
            produtos.append(input("===Cadastar Produto===\nProduto: "))
            print("Produto cadastrado.\n")
        elif opcao == "2":
            print("===Produtos Listados===")
            for produto in produtos:
                print(produto)
            print("")
        elif opcao == "3":
            buscar = input("===Buscar Produto===\nProduto: ")
            if buscar in produtos:
                print("Produto listado.")
            else:
                print("Produto não listado.")
        elif opcao == "4":
            produtos.remove(input("===Remover Produto===\nProduto: "))
            print("Produto removido.\n")
        elif opcao == "5":
            with open(input("Nome do arquivo: "),"w", encoding="utf-8") as arq:
                arq.write("===Backup===\n",)
                for produto in produtos:
                    arq.write(produto)
                    arq.write("\n")
        elif opcao == "6":
            with open(input("Nome do arquivo: "),"r", encoding="utf-8") as arq:
                print(arq.read())
        elif opcao == "0":
            print("Encerrando sistema...")
        else:
            print("Opção invalida.\n")
menu()