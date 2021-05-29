num  = int(input('Please enter a number: '))

if num > 1:
    composite = [i for i in range(2, num )if num % i == 0]
    print( num, ' is a composite number and the factors:', composite)
    