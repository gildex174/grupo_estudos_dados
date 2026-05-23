import re

email = input("Diga seu email: \n")

if re.search(r"^\w+@(\w+\.)?\w+\.com$", email, flags=re.IGNORECASE):
    print("Válido!")
else:
    print("Email no formato incorreto...")
