vogais = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú", "à", "è", "ì", "ò", "ù", "ã", "õ"]
frase = str(input("Digite uma frase: ").lower())
letras = list(frase)
qnt = 0
for caractere in letras:
    if caractere in vogais:
        qnt += 1
print(f"Quantidade de vogais: {qnt}")