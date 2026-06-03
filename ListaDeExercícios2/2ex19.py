def portas():
    while True:
        porta = int(input("===Firewall | Validador de portas de rede===\nDigite uma porta: "))
        if porta == 80 or porta == 443:
            print("Porta liberada.")
            break
        else:
            print("Porta negada. Tente novamente.")
portas()