alunos_impares = []
alunos_pares = [] 
media_impares = 0;
media_pares = 0;

for aluno in range(1, 51):
  if (aluno % 2 == 0):
    alunos_pares.append(aluno)
  else:
    alunos_impares.append(aluno)

print("Você está digitando a nota dos alunos ímpares!")
    
for aluno in alunos_impares:
  nota = float(input("Por favor, insira a nota do aluno de número {}:".format(aluno)))
  media_impares += nota
  
print("A média dos alúnos impares é: {:.2f}".format(media_impares / len(alunos_impares)))

print("Você está digitando a nota dos alunos pares!")
    
for aluno in alunos_pares:
  nota = float(input("Por favor, insira a nota do aluno de número {}: ".format(aluno)))
  media_pares += nota
  
print("A média dos alúnos pares é: {:.2f}".format(media_pares / len(alunos_pares)))

if (media_pares / len(alunos_pares)) > (media_impares / len(alunos_impares)):

    print("Os alunos pares obtiveram a maior média")

else:
    print("Os alunos impares obtiveram a maior média")
    
