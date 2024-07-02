def filtrar_palavras_por_letra(lista_palavras, letra):
    palavras_filtradas = []
    for palavra in lista_palavras:
        if palavra.lower().startswith(letra.lower()):
            palavras_filtradas.append(palavra)
    return palavras_filtradas

def main():
    lista_palavras = ["Abacate", "Abacaxi", "Açaí", "Acerola", "Amora", "Ameixa", "Banana", "Caju", "Cereja", "Coco", "Damasco", "Figo", "Goiaba", "Groselha", "Jabuticaba", "Jaca", "Kiwi", "Laranja", "Limão", "Maçã", "Mamão", "Manga", "Maracujá", "Melancia", "Melão", "Morango", "Pera", "Pêssego", "Pitanga", "Pitaya", "Romã", "Tangerina", "Uva"]
    letra = input("Digite uma letra para filtrar as palavras: ")
    palavras_filtradas = filtrar_palavras_por_letra(lista_palavras, letra)
    print(f"Palavras que começam com '{letra}':")
    for palavra in palavras_filtradas:
        print(palavra)

if __name__ == "__main__":
    main()
