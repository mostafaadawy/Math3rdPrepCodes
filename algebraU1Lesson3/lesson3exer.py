#Three lines to make our compiler able to draw:
import sys
import math
import matplotlib.pyplot as plt

X=range(-10,10)

def fn(x):

    return (-10)*x+80

images=set()
print('f ={',end='')
for x in X:
    images.add(fn(x))
    plt.scatter([x],[fn(x)])
    print('(',x,',',fn(x),'),',end='')
print('}')    
print('range=',images)
print('X=',X)
print('f(x)=',images)

plt.show()
#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()