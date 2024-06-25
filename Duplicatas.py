def remover_duplicatas(lista):
    lista_sem_duplicatas = []
    for elemento in lista:
        if elemento not in lista_sem_duplicatas:
            lista_sem_duplicatas.append(elemento)
    return lista_sem_duplicatas

def main():
    lista_original = input("Digite os elementos da lista separados por espaço: ").split()
    lista_sem_duplicatas = remover_duplicatas(lista_original)
    print("Lista sem duplicatas:", lista_sem_duplicatas)
