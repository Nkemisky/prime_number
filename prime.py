num  = int(input('Please enter a number: '))
index = []

if num > 1:
    composite = [i for i in range(2, num )if num % i == 0] 
    if composite == []:
        prime = [i for i in range(2, num )if num // i != 0]
        print( num, 'is a prime number and the factors:', 1,num)
        index = num - 2
        print('With 1st method number of iteration is:', index )
    else:
        print( num, 'is a composite number and the factors:', composite)
        index = num - 2
        print('With 1st method number of iteration is:', index )

    
