#Three lines to make our compiler able to draw:
import sys
import numpy as np
import math
from scipy.interpolate import make_interp_spline as intr
import matplotlib.pyplot as plt

X=np.array([-4,-3,-2,-1,0,1,2])


def fn(x):
    return (x*x)+(2*x)-3

fx=[]
rang=set()
print('f ={',end='')
for x in X:
    fx.insert(0,fn(x))
    rang.add(fn(x))
    print('(',x,',',fn(x),'),',end='')
print('}')    
print('range=',rang)
print('X=',X)
print('f(x)=',fx)
plt.title("quadratic function")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

XYInter = intr(X, fx)
X_ = np.linspace(X.min(), X.max(), 500)
fx_ = XYInter(X_)
plt.plot(X_,fx_)

plt.show()
#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()


