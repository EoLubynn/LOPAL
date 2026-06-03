kg = int(input("===Calculadora IMC===\nPeso (Kg): "))
hcm = int(input("Altura (Cm): "))
hm = hcm / 100
IMC = kg / hm ** 2
print(f"IMC: {IMC:.2f}")