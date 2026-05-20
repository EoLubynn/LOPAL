chamados = ["T001", "T002", "T003", "T004"]

def menu():
        while True:
            print("\n===Execuções===\n1.Adicionar Ticket;\n2.Remover Ticket;\n3.Chamados Pendentes;\n4.Sair.")
            opcao = input("Digite a opção que deseja.\n")
            if opcao == "Adicionar" or opcao == "adicionar" or opcao == "1":
                chamados.append(input("Digite a tag do ticket:\n"))
            elif opcao == "Remover" or opcao == "remover" or opcao == "2":
                chamados.remove(input("Digite a tag do ticket:\n"))
            elif opcao == "Chamados Pendentes" or opcao == "chamados pendentes" or opcao == "chamados" or opcao == "Chamados" or opcao == "3":
                print("===Chamados Pendentes===")
                for chamado in chamados:
                    print(chamado)
            elif opcao == "Sair" or opcao == "sair" or opcao == "4":
                print("Encerrando serviço...")
            else:
                print("Opção invalida!")
menu()




