nota = int(input("Qual foi a sua nota? \n"))

if 90 <= nota:
    print("Você tirou A!")
elif 80 <= nota:
    print("Você tirou B!")
elif nota >= 70 and nota <= 79:
    print("Você tirou C...")
elif nota >= 60 and nota <= 69:
    print("Você tirou D...")
else:
    print("Você tirou F ;(")
