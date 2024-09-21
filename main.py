numeros_pares = 0
for dragonball in range(5):
    valor = int(input(f"Digite o {dragonball+1}º valor inteiro: "))
    if valor % 2 == 0:
        numeros_pares += 1
print(f"Total de números pares digitados: {numeros_pares}")