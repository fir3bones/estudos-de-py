import math
cato= int(input('Qual o cateto oposto de um triangulo? '))
cata= int(input('Qual o cateto adjacente? '))
hipo= math.hypot(cato, cata)

print('O comprimento da hipotenusa é {:.0f}'.format(hipo))


#math.hypot(cato, cata) quando for calular hipotenusa