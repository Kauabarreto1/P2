entrada = input("Digite uma lista de números separados por espaços: ")
numeros = list(map(int, entrada.split()))
if len(numeros) == 0:
    print("A lista está vazia.")
else:
    maior = numeros[0]
    menor = numeros[0]

    for num in numeros:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    print(f"O maior número é: {maior}")
    print(f"O menor número é: {menor}")