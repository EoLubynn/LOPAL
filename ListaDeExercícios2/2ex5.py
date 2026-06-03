ebook = int(input("===E-Books===\nValor do E-Book: R$"))
if ebook > 80:
    desconto = ebook * 0.9
    print(f"\n===Compra===\nPreço: R${ebook}\n(Desconto: 10%)\nValor Final: R${desconto}")
else:
    print(f"\n===Compra===\nPreço: R${ebook}\nValor Final: R${ebook}")