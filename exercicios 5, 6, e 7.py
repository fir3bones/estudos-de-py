#Exercício 5 e 6

n1=int(input('um numero: '))
#exerc.5
a=n1-1
b=n1+1
#exerc.6
d=n1*2
t=n1*3
r=n1**2

print('o sucessor de {} é {} e o antecessor é {}'.format(n1, b, a))
print('O Dobro {}, Triplo {} e Raíz quadrada {}'.format(d, t, r))

#exerc 7

nome=input('Qual o nome do aluno? ')
n2=int(input('Qual a nota da primeira prova? '))
n3=int(input('Qual a nota da segunda prova? '))
m=(n2+n3)/2

print('A média de {} é {} '.format(nome, m))
