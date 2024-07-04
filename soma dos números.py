soma = 0
while True:
    numero = int(input("Digite um número (ou 0 para sair): "))
    soma += numero
    if numero == 0:
        break
print(f"A soma dos números digitados é: {soma}")
