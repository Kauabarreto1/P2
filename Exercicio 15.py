comidas = ['leite', 'couve','computador', 'tomate','garfo','faca','tablet','refrigerante']
bebidas = ['uva', 'colher','TV','vinho','cerveja','celular','banana']
talheres = ['arroz','iPhone', 'concha','whisky','vodka','feijão','colher de chá']
eletronicos = []
eletronicos.append('computador')
eletronicos.append('tablet')
eletronicos.append('TV')
eletronicos.append('celular')
eletronicos.append('iPhone')
comidas.remove('leite')
comidas.remove('computador')
comidas.remove('garfo')
comidas.remove('faca')
comidas.remove('refrigerante')
comidas.remove('tablet')
comidas.append('uva')
comidas.append('banana')
comidas.append('arroz')
comidas.append('feijão')
bebidas.remove('uva')
bebidas.remove('colher')
bebidas.remove('TV')
bebidas.remove('celular')
bebidas.remove('banana')
bebidas.append('leite')
bebidas.append('refrigerante')
bebidas.append('vodka')
bebidas.append('whisky')
talheres.remove('arroz')
talheres.remove('whisky')
talheres.remove('iPhone')
talheres.remove('vodka')
talheres.remove('feijão')
talheres.append('garfo')
talheres.append('faca')
talheres.append('colher')
print (f"comidas {comidas}")
print (f"bebidas {bebidas}")
print (f"talheres {talheres}")
print (f"eletronicos {eletronicos}")