import re

email = input("Diga seu email: \n")

if re.search(r"^\w+@\w+\.com$", email):
    print("Válido!")
else:
    print("Email no formato incorreto...")
