#primeiro metodo utilizado

import math
num = float(input('Digite um número real: '))
num2= math.trunc(num)

print('O número {} tem a parte inteira {}'.format(num, num2))

#segundo metodo utilizado

import math
num=float(input('Digite um número real: '))

print('O número {} tem a parte inteira {}'.format(num, math.floor(num)))


#IMPORTANTE NÃO ESQUECER ANIMAL... QUANDO FOR FAZER PRINT NAO COLOCAR UM = NA FRENTE DELE