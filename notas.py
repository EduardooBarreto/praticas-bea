# --------------------------------------------
# notas alunos

nota = float(input())

match nota:
    case _ if nota < 0: print("Invalido")
    case _ if nota < 5: print("insuficiente")
    case _ if nota < 7: print("regular")
    case _ if nota < 9: print("Bom")
    case _ if nota <= 10: print("Excelente")
    case _: print('invalido')
    

