MB = int(input("===Tempo de Download===\nTamnho do arquivo (Megabyte): "))
Mb = MB * 8
Mbps = int(input("Velocidade de download: ")) 
tempo = Mb / Mbps
print(f"Tempo estimado de download: {int(tempo)} Mb/seg.")