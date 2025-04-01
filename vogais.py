# --------------------------------------------
# é vogal?

vogal = input().lower()
match vogal:
    case _ if vogal in 'aeiou': print('é vogal')
    case _: print("Não é vogal")