lista = []
while True:
    elemento = input("Digite um elemento para adicionar à lista (digite 'parar' para encerrar): ")
    if elemento.lower() == 'parar':
        break
    lista.append(elemento)
print("Lista completa:")
print(lista)