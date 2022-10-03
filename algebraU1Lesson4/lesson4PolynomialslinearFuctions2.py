#Three lines to make our compiler able to draw:
import sys
import math
import matplotlib.pyplot as plt


X=range(-5,5)


def minusHalfX(x):
    return -0.5*x

# 1-get the projections or range
images=set()
for x in X:
    #images.add(x*x-1)
    images.add(minusHalfX(x))
print('range',images)

print('f set ={',end='')
for x in X:
    print('(',x,',',minusHalfX(x),'),',end='')
    plt.scatter([x],[minusHalfX(x)])
print('}')

plt.show()
#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()