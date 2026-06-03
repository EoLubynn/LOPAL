bolsa = float(input("===Bolsa Auxílio===\nValor atual da bolsa auxílio: R$"))
if bolsa < 1000:
    reajuste = bolsa * 1.15
elif bolsa >= 1000:
    reajuste = bolsa * 1.10
print(f"\n===Reajuste===\nValor atual da bolsa de auxílio: R${reajuste:.2f}")