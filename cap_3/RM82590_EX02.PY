alunosImpares = []
alunosPares = [] 
mediaImpares = 0;
mediaPares = 0;

for aluno in range(1, 51):
  if (aluno % 2 == 0):
    alunosPares.append(aluno)
  else:
    alunosImpares.append(aluno)

print("Você está digitando a nota dos alunos ímpares!")
    
for aluno in alunosImpares:
  nota = float(input("Por favor, insira a nota do aluno de número {}:".format(aluno)))
  mediaImpares += nota
  
print("A média dos alúnos impares é: {:.2f}".format(mediaImpares / len(alunosImpares)))

print("Você está digitando a nota dos alunos pares!")
    
for aluno in alunosPares:
  nota = float(input("Por favor, insira a nota do aluno de número {}: ".format(aluno)))
  mediaPares += nota
  
print("A média dos alúnos pares é: {:.2f}".format(mediaPares / len(alunosPares)))

if (mediaPares / len(alunosPares)) > (mediaImpares / len(alunosImpares)):

    print("Os alunos pares obtiveram a maior média")

else:
    print("Os alunos impares obtiveram a maior média")
    
