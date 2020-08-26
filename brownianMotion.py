import numpy as np
import matplotlib.pyplot as plt 

def wiener_process(T,N):
    """
    T: total time 
    N: total number of steps 
    """
    W0 = [0]
    dt = T / float(N)

    # simulate the increments by 
    # normal random variable generator  
    increments = np.random.normal(0, 1*np.sqrt(dt), N)
    W = W0 + list(np.cumsum(increments))
    return W

N = 1000
T = 10
dt = T / float(N)
t = np.linspace(0.0, N*dt, N+1)
plt.figure(figsize=(15,10))

for i in range(5):
    W = wiener_process(T,N)
    plt.plot(t, W)
    plt.xlabel('time')
    plt.ylabel('W')
    plt.grid(True)
    
plt.show()