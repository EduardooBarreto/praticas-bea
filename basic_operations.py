# --------------------------------------------
# Receba dois números e faça as 4 operaçõoes basicas.
# Use um caso default para operações inválidas

# números
numero1, numero2 = float(input()), float(input())

# operação
operatino = print("""Que operação deseja realizar?:\n
[1] Soma\n
[2] Subtração\n
[3] Multiplicação\n
[4] Divisão\n""")

# casos
match int(input("Resposta: ")):
    case 1:
        print(f"A soma de {numero1} + {numero2} é {numero1 + numero2}")
    case 2:
        print(f"A Subtração de {numero1} por {numero2} é {numero1 - numero2}")
    case 3:
        print(f"A Multiplicação de {numero1} por {numero2} é {numero1 * numero2}")
    case 4:
        print(f"A Divisão de {numero1} por {numero2} é {numero1 / numero2}") if not numero2 == 0 else print("Não é possível dividir por 0")
    case _:
        print("Operação inválida")


    

        

