temp = int(input("===Temperatura do Servidor===\nTemperatura atual (ºC): "))
if temp >= 75:
    print("\n===Alerta===\nSuperaquecimento detectado!")
else:
    print("\n===Registro de Temperatura===\nTemperatura normal.")