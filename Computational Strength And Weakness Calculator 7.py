# (Computational) Strength And Weakness Calculator

import pandas as pd
import time
import csv

## 1.0 input
datetime = time.localtime()
observable = input('describe the observation: ')
pot_energy = float(input('potential energy / work: [J / Nm] '))
time_1 = float(input('lasting duration or age (time): [ s] '))
time_2 = float(input('lasting duration (time): [s] '))
money = float(input('price or money: (e.g.[€]) '))

## 2.0 transformation

'''
x1 ... observable
m ... mass
t ... time
r ... position
M ... money
v = d/t ... velocity
a = v/t ... acceleratiom
F = m*a ... force
W = F * d = E ...work or energy
P = W / t ... power
E = P * mf1 ... energy
mf ... modifying factor 1
sR = P / t ... simple robustness
sSt = sR / M ... simple strength
sWk = sR / -M = -sSt ... simple weakness
'''
power = pot_energy/time_1
simple_robustness = power/time_2
energy_price = pot_energy/money
power_price = power/money
simple_strength = simple_robustness/money
simple_weakness = (simple_robustness/money)*(-1)

### 2.1 updating
'''data_entry = (datetime,set,simple_strength)
print(data_entry)
'''
#### 2.1.1 writing results to a .csv document


### 2.2 storing sets into a pandas dataframe and sorting descending
'''
simple_strength_data = pd.read_csv('simple strength data.csv')
'''
### 2.3 storing the updated strongest set in the the_strong variable
'''
print(simple_strength_data.head(1))
the_strong = simple_strength_data.head(1)
'''
### 2.4 normalizing and visualizing

### 2.5 normalizing

### 2.6 visualizing


## 3.0 output

'''
print('-------------------\n')
print(datetime)
print('-',set)
print('Energy Per Money: ',energy_price, 'J/M')
print('Power Per Money: ',power_price, 'W/M')
print('Simple Strength: ',strength, 'W/sM')

the_strong = 'wheat flour'

print('\n---------\n>',the_strong)
'''

if simple_strength > 0:
	print('\n------\nSimple Strength: ',simple_strength, 'W/sM or sSt')
elif simple_strength < 0:
	print('\n------\nSimple Weakness: ',simple_strength, 'W/sM or sWk')
elif simple_strength == 0:
	print('------\nYou have got whether a strength nor a weakness. (0 W/sM)')
