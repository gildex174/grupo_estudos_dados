import sys


if len(sys.argv) < 2:
    print("Erro!!")
    sys.exit()



for arg in sys.argv[1:]:
    print(f"Olá, {arg}")

for i in range(1, len(sys.argv)):
    print(sys.argv[i])