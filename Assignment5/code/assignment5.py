import numpy as np
import math
import matplotlib.pyplot as plt

alpha=math.pi/6
beta=math.pi/3
c=2
a=np.array([np.cos(alpha)*c, np.sin(alpha)*c])
b=np.array([np.cos(beta)*c,np.sin(beta)*c])
distance=math.sqrt((a-b).T@(a-b))
print(distance)