def urna():
    Alice = 0
    Bob = 0
    while True:
        opcao = int(input("===Lista de Candidatos===\nAlice - 1\nBob - 2\nSair - 0\nDigite o número para votar: "))
        if opcao == 1:
            Alice += 1
            print("Voto constatado: Alice\n")
        elif opcao == 2:
            Bob += 1
            print("Voto constatado: Bob\n")
        elif opcao == 0:
            print("Opção de sair selecionada.")
            print(f"\n===Votos===\nAlice: {Alice}\nBob: {Bob}")
            break
        else:
            print("Opção invalida!\n")
urna()