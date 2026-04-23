#Exerc.11

a=int(input('qual é a altura da parede em metros? '))
l=int(input('qual é a largura da parede em metros? '))
area=a*l
result=(a*l)/2

print(f'para pintar a parede voce irá precisar de {result:.0f} litros de tinta')

#Exerc.12

preço=float(input('Preço do produto: '))
desconto=int(input('Desconto: '))
d=preço*(1-desconto/100)

print('O valor do produto é:',preço,'reias')
print(f'E com 5% de desconto o valor passa a ser {d} reias')

#Exerc.13

salario=float(input('Qual é o salário de joão? '))
aumento=int(input('Aumento: '))
rf=salario*(1+aumento/100)

print('O salário de João é:', salario,'reais')
print(f'E com 15% de aumento o salário passa a ser {rf:.0f} reais')