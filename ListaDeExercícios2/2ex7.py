ip = int(input("===Endereço IP===\nIP: "))
if ip >= 1 and ip <= 126:
    print("IP Classificado: Classe A")
elif ip >= 128 and ip <= 191:
    print("IP Classificado: Classe B")
elif ip >= 192 and ip <= 223:
    print("IP Classificado: Classe C")
else:
    print("IP não classificado.")
    