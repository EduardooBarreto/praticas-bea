# --------------------------------------------
# dias úteis e não úteis

match int(input('digite um número de 1 a 7: ')):
    case 1: print("Segunda-feira: Dia útil")
    case 2: print("Terça-feira: Dia útil")
    case 3: print("Quarta-feira: Dia útil")
    case 4: print("Quinta-feira: Dia útil")
    case 5: print("Sexta-feira: Dia útil")
    case 6: print("Sábado: Dia não útil")
    case 7: print("Domingo: Dia não útil")
    case _: print('inválido')