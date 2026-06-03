resultado = 1
n = int(input("===Fatorial Simples===\nDigite um número: "))
for i in range(n, 0, -1):
    resultado *= i
print(f"Fatorial de {n}: {resultado}")

