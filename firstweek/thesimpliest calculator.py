n1 = input('Enter a number (or a letter to exit): ')
alpha = ['a,b,c,d.......z']
if n1 is alpha:
    print('Exit')
else:
    operation = input('Enter an operation (+,-,,/): ')
    n2 = int(input('Enter another number: '))
    result = 0
    if operation == '+':
        result = int(n1) + n2
    if operation == '-':
        result = int(n1) - n2
    if operation == '':
        result = int(n1) * n2
    if operation == '/':
        result = int(n1) / n2
    print('Result: ', result)