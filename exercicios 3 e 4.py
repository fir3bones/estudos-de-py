n1 = int(input('escreva um número: '))
n2 = int(input('escreva outro: '))
res = n1+n2
nome = input('escreva um nome: ')

print('a soma de {} e {} é igual a {}'.format(n1, n2, res))
print('o nome {}'.format(nome), type(nome))
print(nome.isalnum())
print(nome.isalpha())
print(nome.isdecimal())