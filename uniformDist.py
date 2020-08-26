import random
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd 

# function to simulate rolling a dice
def dice():
    number = [1,2,3,4,5,6]
    return random.choice(number)

# create a series of random variables
series = np.array([dice() for x in range(10000)])

print(series)

plt.figure(figsize=(20,10))
plt.hist(series, bins=11, align='mid')
plt.xlabel('Dice Number')
plt.ylabel('Occurences')
plt.grid()
plt.show()

# frequenct that observations are less than or equal to 3 
# P(x<=3)
print(len([x for x in series if x<=3])/float(len(series)))
print(np.mean(series))

