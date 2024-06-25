def concatenar_listas(lista1, lista2):
    lista_concatenada = []
    for elemento in lista1:
        lista_concatenada.append(elemento)
    for elemento in lista2:
        lista_concatenada.append(elemento)
    return lista_concatenada

def main():
    elementos_lista1 = input("Digite os elementos da primeira lista separados por espaço: ").split()
    elementos_lista2 = input("Digite os elementos da segunda lista separados por espaço: ").split()
    lista_concatenada = concatenar_listas(elementos_lista1, elementos_lista2)
    print("Listas concatenadas:", lista_concatenada)

if __name__ == "__main__":
    main()
