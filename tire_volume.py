import math
from datetime import datetime
with open('volumes.txt') as volumes:
  
    tire=('1')
    while tire=='1':   #the %Y-%m-%d will print only the date and not the time
        dt= datetime.now()
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
        print(f'{volumes}')
        print()
        print(f'{dt:%Y-%m-%d}, {w}, {a}, {d}, {v:.2f}')
        print()
        tire=input('If you want to enter another tire, press "1+enter". To end press enter: ')
        print()
    print('Have a good day!')