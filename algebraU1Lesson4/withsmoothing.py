#Three lines to make our compiler able to draw:
import sys

import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline as intr


X=np.array([-4,-3,-2,-1,0,1,2])


def fn(x):
    return (x*x)+(2*x)-3

# 1-get the projections or range
images=set()
fx=[]
print('f ={',end='')
for x in X:
  fx.insert(0,fn(x))
  images.add(fn(x))
  print('(',x,',',fn(x),'),',end='')
print('}')    
print('range=',images)
print('X=',X)
print('f(x)=',fx)

XYInter = intr(X, fx)
X_ = np.linspace(X.min(), X.max(), 500)
fx_ = XYInter(X_)

plt.plot(X_,fx_)
plt.title("quadratic function")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()
#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()




