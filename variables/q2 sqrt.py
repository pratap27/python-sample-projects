# without math module, and using ** operator

''' num = float(input('Enter a Number to find Square root: '))

num_sqrt = num ** 0.5

print('The sqrt of %0.2f is %0.2f'%(num,num_sqrt)) '''

# from math module

''' import math

num = float(input('Enter a Number to find Square root: '))

num_sqrt = math.sqrt(num)

print('The sqrt of %0.2f is %0.2f'%(num,num_sqrt)) '''


# sqrt for complex numbers

import cmath

num = eval(input('Enter a complex Number to find Square root: '))

num_sqrt = cmath.sqrt(num)

print('The sqrt of {0} is {1:0.3f}+{2:0.3f}j'.format(num, num_sqrt.real, num_sqrt.imag))
