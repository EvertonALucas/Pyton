import random
print("\n* * * SORTEANDO TRÊS NÚMEROS DIFERENTES ENTRE 1 E 50 * * *\n")
input("Pressione ENTER para gerar os números: ")
while True:
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    num3 = random.randint(1, 50)
    if num1 not in (num2, num3) and num2 != num3:
        break
print("Os números são:\n ", num1, num2, num3)
input("Pressione ENTER para sair...")
