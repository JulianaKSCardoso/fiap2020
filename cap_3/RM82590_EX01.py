alimentosIngeridos = int(input("Insira a quantidade de alimentos ingeridos: "))
totalCalorias = 0

for alimento in range(1, alimentosIngeridos + 1):
  calorias = float(input("Informe a quantidade de calorias do {}º alimento: ".format(alimento)))
  totalCalorias += calorias
  
print("Você ingeriu {} calorias" .format(totalCalorias))