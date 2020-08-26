import random
import pandas as pd 
import math
import matplotlib.pyplot as plt 
# success rate: p=0.7
# experiment times: n=10

def trial():
    number = [1,2,3,4,5,6,7,8,9,10]
    a = random.choice(number)

    if(a<=7):
        return 1
    else:
        return 0

# each time we execute trial, will run an experiment
# success = 1, failure = 0
# do experiment 10 times

result = [trial() for x in range(10)]
print(sum(result))

# for binomial distribution, need experiment N times 
def binomial(number):
    l = []
    for i in range(10000):
        result = [trial() for x in range(10)]
        l.append(sum(result))
    return len([x for x in l if x==number])/float(len(l))

print("If we experiment 10 times, and succeed 8 times, then the simulated probability is {}".format(binomial(8)))

# for each possible outcome, we simulate the probability
prob = []

for i in range(1,11):
    prob.append(binomial(i))

prob_s = pd.Series(prob, index=range(1,11))
print(prob_s)

# plot the results
plt.figure(figsize = (20,10))
plt.bar(range(1,11), prob)
plt.grid()
plt.show()
