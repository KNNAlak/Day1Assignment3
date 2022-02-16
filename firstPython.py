import pandas as pd
x = float(input('Please input the length of the room: '))
y = float(input('Please input the width of the room: '))
z =  float(input('Please input the length of the door: '))
print(f'room area that need to be covered: ', x*y)
print(f'room perimeter that need to be installed baseboard :', 2*(x+y)-z)
