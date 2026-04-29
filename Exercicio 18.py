import math
n1=math.radians(float(input('Digite um angulo: ')))
cos=math.cos(n1)
sen=math.sin(n1)
tan=math.tan(n1)

print('O coseno de {} é {}, o seno é {}, e a tangente é {}'.format(n1, cos, sen, tan))


#lembrar sempre no n1 colocar math.radians, o resto estava perfeito...