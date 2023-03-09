import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(-10.0, 10.0, 500)
ratio = np.exp(-abs(x)+abs(x-1))

print('Name : Aniket Chauhan')
print('Roll Number : MT20030')
plt.figure(figsize = (10, 5)) 
plt.plot(x, ratio)
plt.xlabel('x') 
plt.ylabel('p(x/w1)/p(x/w2)')
plt.grid()
plt.show()