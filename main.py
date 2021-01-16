import addition
import substraction
import multiplication
import division

a = int(input('Enter first number : '))
b = int(input('Enter second number : '))
op = input('Enter the operator : ')

if op == '+':
    print(addition.add(a, b))
elif op == '-':
    print(substraction.sub(a, b))
elif op == '*':
    print(multiplication.multiply(a, b))
elif op == '/':
    print(division.div(a, b))
else:
    print('Invalid operator')

