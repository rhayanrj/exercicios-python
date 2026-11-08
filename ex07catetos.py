import math


lado_a = float(input('digito o valor do cateto a:\n'))
lado_b = float(input('digito o valor do cateto b:\n'))
print('o valor da hipotenusa é {:.2f}'.format(math.hypot(lado_a, lado_b)))