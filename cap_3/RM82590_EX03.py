minutosAtuais = int(input("Insira os minutos atuais: "))
fatorial = 1

for minuto in range(1, minutosAtuais + 1):
  fatorial *= minuto
  
print("A senha é: LIBERDADE{}".format(fatorial))