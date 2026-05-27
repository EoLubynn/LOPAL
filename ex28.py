alunos = []
notas = []
def boletim():
    while True:
        print("===Boletim===\nInsira o boletim dos alunos abaixo.")
        for i in range(5):
            alunos.append(str(input("Aluno: ")))
            notas.append(float(input("Nota: ")))
        for aluno in alunos:
            for nota in notas:
                print("Aluno: ", aluno, "\nNota: ", nota)
                if nota >= 7:
                    print("Resultado: Aprovado.")
                else:
                    print("Resultado: Reprovado.")
        break
boletim()

