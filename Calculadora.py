print("As operaçôes são:")
print("+ Adição")
print("- Subtração")
print("* Multiplicação")
print("/ Divisão")
a = float(input("Digite o primeiro número da equação: "))
op = str(input("Digite a operação: "))
b = float(input("Digite o segundo número da equação: "))
if op == '+':
    print(a+b)
elif op == '-':
    print (a-b)
elif op == '*':
    print (a*b)
elif op == '/':
    print (a/b)
else :
    print ("ERROR")