#Three lines to make our compiler able to draw:
import sys

import math
import matplotlib.pyplot as plt

X=[-2,-1,0,1,2,3,4]


def fn(x):
    return (x*x)-(2*x)-3

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
plt.plot(X,fx)
plt.title("quadratic function")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()
#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()




