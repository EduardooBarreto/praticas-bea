# --------------------------------------------
# 12, 17, 59, 60>, inválido

idade = int(input())
match idade:
    case _ if idade <= 0:
        print('inválido')
    case _ if idade <= 12:
        print('Criança')
    case _ if idade <= 17:
        print('Adolescente')
    case _ if idade <= 59:
        print('Adulto')
    case _ if idade >= 60:
        print('Idoso')

        
