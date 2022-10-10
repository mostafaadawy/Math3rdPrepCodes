#Three lines to make our compiler able to draw:
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline as intr

#X=range(-5,12)
X=np.array(range(-5,12))
def fn(x):
    return (-x)*x+6*x+7

fx=[]
plt.title("quadratic function")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
print('f ={',end='')
for x in X:
    fx.insert(0,fn(x))
    print('(',x,',',fn(x),'),',end='')
print('}')    
print('range=',set(fx))
print('X=',X)
print('f(x)=',fx)

XYInter = intr(X, fx)
X_ = np.linspace(X.min(), X.max(), 500)
fx_ = XYInter(X_)
plt.plot(X_,fx_)
plt.grid()
plt.show()
#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()