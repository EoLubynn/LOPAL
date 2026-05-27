vendas = [
        [int(input("1º Valor Semanal: ")), int(input("2º Valor Semanal: ")), int(input("3º Valor Semanal: "))],
        [int(input("4º Valor Semanal: ")), int(input("5º Valor Semanal: ")), int(input("6º Valor Semanal: "))],
        [int(input("7º Valor Semanal: ")), int(input("8º Valor Semanal: ")), int(input("9º Valor Semanal: "))]
]

print("===Valores Semanais===")
for semana in vendas:
    print(semana)
print("===Valores | 3 Semanas===")
total = 0
for semana in vendas:
    totals = sum(semana)
    print("Total da Semana: R$", totals)
    total += totals
print("===Valor Total===\nTotal: R$", total)
melhor = 0
for semana in vendas:
    if max(semana) > melhor:
        melhor = max(semana)
print("===Maior Venda===\nMelhor Receita: R$", melhor)
