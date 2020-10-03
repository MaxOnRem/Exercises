import math

# Ремез Максим Варіант 1 (МІТ)

a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))
x1 = float(input('Enter x1: '))
x2 = float(input('Enter x2: '))
while x1 > x2:
        print('Error, %s > %s, enter other values'% (x1, x2) )
        x1 = float(input('Enter X1: '))
        x2 = float(input('Enter X2: '))
step = float(input('Enter step: '))
if step <=0:
    print("Step doesn't exist")
while step <=0:
    step = float(input('Enter other step: '))

while x1 < x2:
    if x1 < 0 and b!=0:
        print('F = ', round(a * math.pow(x1) + b, 3),',','x =',x1)
    elif x1 > 0 and b == 0:
        if x1 - c != 0:
            print('F = ', round((x1 - a) / (x1 - c), 3),',','x =',x1)
        else:
            print("Error: denominator equals 0, that's impossible")

    else:
        if c == 0:
            print("Error, c can't be 0")
        else:
            print("F = ", round((x1 / c), 3),',','x =',x1)
    x1 = round(step + x1, 3)
