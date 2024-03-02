import math
from datetime import datetime
with open('volumes.txt', 'at') as volumes:
    options=['1. Add tire', '2. View tires', '3. Quit']
    tire=''
    print('------------------------------------------------------------')

    while tire!=3:   #the %Y-%m-%d will print only the date and not the time
        dt= datetime.now()
        print()
        print('Please select one of the following: ')
        options=['1. Add tire', '2. View tires', '3. Quit']
        
        for opt in options:
            print()
            print(opt)
        print()
        try:
            tire=int(input('Please choose an action (enter #1-3): '))
            print()
        except ValueError:
            print('------------------------------------------------------------')
            print()
            print('That is not an option, please try again')
        print()
        print('------------------------------------------------------------')

        print()
        w= int(input('Enter the Width of Tire in mm: '))
        print()
        a= int(input('Enter the Aspect Ratio of tire: '))
        print()
        d= int(input('enter the diameter of the wheel in inches: '))
        print()

        pi= math.pi
        v= pi * w**2 * a * (w * a + 2540 * d) / 10000000000

        print(f'The approxamite volume is {v:.2f} liters')
        print()
        print(f'{dt:%Y-%m-%d}, {w}, {a}, {d}, {v:.2f}', file=volumes)
        print()
        
        for opt in options:
            print()
            print(opt)
        print()
        try:
            tire=int(input('Please choose an action (enter #1-3): '))
            print()
        except ValueError:
            print('------------------------------------------------------------')
            print()
            print('That is not an option, please try again')
        print()
        print('------------------------------------------------------------')






        print()
    # print(volumes)
    print()
    print('Have a good day!')
    print()