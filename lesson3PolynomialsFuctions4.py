#Three lines to make our compiler able to draw:
import sys
import math
import matplotlib.pyplot as plt


X={1,0,-2,0.5,math.sqrt(5),2*math.sqrt(2)+1,1-math.sqrt(2)}


def polynomial1(x):
    return x*x-(2*x)+5

# 1-get the projections or range
images=set()
for x in X:
    #images.add(x*x-1)
    images.add(polynomial1(x))
print('range',images)

print('f set ={',end='')
for x in X:
    print('(',x,',',polynomial1(x),'),',end='')
    plt.scatter([x],[polynomial1(x)])
print('}')

plt.show()
#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()