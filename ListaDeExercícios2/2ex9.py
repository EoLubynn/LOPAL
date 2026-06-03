falta = float(input("===Monitoramento de Presença===\nPercentual de faltas: "))
if falta >= 12.5:
    print("\n===Alerta===\nLimite de faltas atingido!")
else:
    print("\nAluno dentro da safe zone.")