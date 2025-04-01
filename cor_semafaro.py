# --------------------------------------------
# Dê uma mensagem dadas as entradas
# vermelho : "Pare! 🤚"
# amarelo : "Atenção! ⚠️"
# verde : "Siga! 🟢"

casos = ["Pare! 🤚", "Atenção! ⚠️", "Siga! 🟢"]

match input():
    case "vermelho": print(casos[0])

    case 'amarelo':  print(casos[1])

    case 'vermelho': print(casos[2])

