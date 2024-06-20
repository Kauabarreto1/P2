n = int(input("Quantas vezes o programa repita? "))
def fibonacci (n):
    fi_sequence = []
    a, b = 0, 1
    for  _ in range(n):
        fi_sequence.append(a)
        a, b = b, a + b 
    return fi_sequence
fi_sequence = fibonacci(n)
print (f"Os primeiros {n} termos da sequência de fibonacci são {fi_sequence}")