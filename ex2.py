numeros = []
par = 0
print("===Digite 10 números abaixo!===")
for i in range(10):
    numeros.append(int(input("Digite um número: ")))
for numero in numeros:
    if numero % 2 == 0:
        print(numero, "- par")
        par += 1
    else:
        print(numero, "- impar")
print("São", par, "números pares!")