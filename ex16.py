np = input("Nome do produto: ")
qp = int(input("Quantidade no estoque: "))
vp = int(input("Quantidade de vendas: "))
print("Estoque restante:", qp - vp)
if qp < vp:
    print("*ALERTA!*\nEstoque vazio ou negativo.")