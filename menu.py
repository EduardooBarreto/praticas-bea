# --------------------------------------------
# restaurante

match int(input("digite um número de 1 a 5: ")):
    case 1: print("Hamburguer : R$15,00")
    case 2: print("Pizza : R$25,00")
    case 3: print("Salada : R$10,00")
    case 4: print("Suco : R$5,00")
    case 5: print("Sorvete : R$7,00")
    case _: print("Inválido")
