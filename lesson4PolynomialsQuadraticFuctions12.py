#Three lines to make our compiler able to draw:
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline as intr

#X={-3,-2,-1,0,1,2,3}
#X=range(-3,4)
X=np.array([-4,-3,-2,-1,0,1,2])


def quadratic(x):
    return (x*x)+(2*x)-3


# get the projections or f(x)
#fx=set()
fx=[]

plt.title("quadratic function")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

for x in X:
    #fx.add(quadratic(x))
    fx.insert(0,quadratic(x))


XYInter = intr(X, fx)
X_ = np.linspace(X.min(), X.max(), 500)
fx_ = XYInter(X_)
plt.plot(X_,fx_)
plt.grid()
print('X=',X)
print('f(x)=',fx)
plt.show()


#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()