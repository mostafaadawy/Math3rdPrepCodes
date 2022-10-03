#Three lines to make our compiler able to draw:
import sys
import math
import matplotlib.pyplot as plt


#X={-3,-2,-1,0,1,2,3}
#X=range(-3,4)
X=[-2,-1,0,1,2,3,4]


def quadratic(x):
    return (x*x)-(2*x)-3


# get the projections or f(x)
#fx=set()
fx=[]

plt.title("quadratic function")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

for x in X:
    #fx.add(quadratic(x))
    fx.insert(0,quadratic(x))
    #plt.scatter([x],[quadratic(x)],s=50)

plt.plot(X,fx)
plt.grid()
print('X=',X)
print('f(x)=',fx)
plt.show()


#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()