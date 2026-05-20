nota = int(input("Insira sua nota: "))
if nota >= 7:
    print("Você foi aprovado!")
elif nota >= 5 and nota <7:
    print("Você está de recuperação!")
else:
    print("Você foi reprovado.")