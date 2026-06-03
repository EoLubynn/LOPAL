palavra = str(input("===Detector de Palíndromo===\nDigite uma palavra: "))
palavra_list = list(palavra)
palindromo = list(reversed(palavra))
if palindromo == palavra_list:
    print(f"A palavra é um palíndromo!\nPalavra: {palavra}\nPalavra ao contrário: {palindromo}")
else:
    print(f"A palavra não é um palíndromo.\nPalavra: {palavra}\nPalavra ao contrário: {palindromo}")