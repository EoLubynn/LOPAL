produtos = []
for i in range(5):
    produtos.append(int(input("Preço do produto: R$")))
subtotal = sum(produtos)
print("Subtotal: R$", subtotal, sep="")
print("Taxa 10%: R$", subtotal * 0.1, sep="")
print("Total: R$", subtotal * 1.1, sep="")