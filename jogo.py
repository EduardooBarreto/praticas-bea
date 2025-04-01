# --------------------------------------------
# joguinho

match int(input("digite um número de 1 a 3: ")):
    case 1: print("You found a treasure! Congrats!")
    case 2: print("You fall into a trap :(!")
    case 3: print("Nothing happened")
    case _: print('invalid')