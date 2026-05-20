n1 = int(input("Primeira nota: "))
n2 = int(input("Segunda nota: "))
n3 = int(input("Terceira nota: "))
media = (n1+n2+n3)/3
if media >=7:
    print("Sua média é de ", media, ".\n Você foi aprovado!", sep="")
elif media >=5 and media <7:
    print("Sua média é de ", media, ".\n Você está de recuperação!", sep="")
else:
    print("Sua média é de ", media, ".\n Você foi reprovado!", sep="")