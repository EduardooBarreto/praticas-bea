# --------------------------------------------
# converta metro em cm, km ou mm

comprimento = float(input("Digite o comprimento em metros"))

match input().lower():
    case 'cm': print(comprimento * 100)
    case 'km': print(comprimento / 1000)
    case 'mm' : print(comprimento * 1000)
    case _: print("inválido")