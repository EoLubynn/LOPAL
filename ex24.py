notas = []
a = 0
print("===Registro de Notas===")
for i in range(10):
    notas.append(float(input("Digite a nota: ")))
notas.sort(reverse=True)
print("===Ranking de Notas===")
for nota in notas:
    a += 1
    print(a, "º - Nota: ", nota)
