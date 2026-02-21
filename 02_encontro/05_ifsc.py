nome = input("Diga um nome: \n")


match nome:
    case "Gildo" | "Ze" | "Artur":
        print("Fiscomper")
    case "Fapesp" | "Brastemp":
        print("Biomoler")
    case "Sofia":
        print("Fisica")
    case _:
        print("Quem????")
