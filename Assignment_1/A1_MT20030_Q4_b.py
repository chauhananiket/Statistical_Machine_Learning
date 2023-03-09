import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(-10.0, 10.0, 500)
p1 = (1/2)*np.exp(-abs(x))
p2 = (1/2)*np.exp(-abs(x-1))

print('Name : Aniket Chauhan')
print('Roll Number : MT20030')
plt.figure(figsize = (10, 5)) 
plt.plot(x, p1,label = 'h') 
plt.plot(x, p2) 
plt.plot([0.5,0.5],[0.0,0.55])
plt.ylabel('Posterior:p(w/x)')
plt.xlabel('x')
plt.legend(["p(w1/x)", "p(w2/x)","Decision Boundary"])
plt.grid()
plt.show()