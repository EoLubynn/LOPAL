cadastro = []
def menu():
    while True:
        print("===Execução===\n1.Cadastrar Usuário;\n2.Remover Usuário;\n3.Listar Usuários;\n4.Sair.")
        opcao = input("\nDigite a opção desejada.\n")
        if opcao == "1" or opcao == "Cadastrar Usuário" or opcao == "cadastrar usuário":
            cadastro.append(input("Usuário: "))
            print("Usuário cadastrado.\n")
        elif opcao == "2" or opcao == "Remover Usuário" or opcao == "remover usuário":
            cadastro.remove(input("Remover Usuário: "))
            print("Usuário removido.\n")
        elif opcao == "3" or opcao == "Listar Usuários" or opcao == "listar usuários":
            print("===Usuários Cadastrados===")
            for usuarios in cadastro:
                print(usuarios)
            print("")
        elif opcao == "4" or opcao == "Sair" or opcao == "sair":
            print("encerrando programação...")
            break
        else:
            print("Opção invalida.")
menu()