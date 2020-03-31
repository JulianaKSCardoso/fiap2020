alimentos_ingeridos = int(input("Insira a quantidade de alimentos ingeridos: "))
total_calorias = 0

for alimento in range(1, alimentos_ingeridos + 1):
  calorias = float(input("Informe a quantidade de calorias do {}º alimento: ".format(alimento)))
  total_calorias += calorias
  
print("Você ingeriu {} calorias" .format(total_calorias))