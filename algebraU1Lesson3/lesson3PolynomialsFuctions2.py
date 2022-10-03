#Three lines to make our compiler able to draw:
import sys

import matplotlib.pyplot as plt


X=range(0,5)


def xplus1(x):
    return x+1

# 1-get the projections or range
images=set()
for x in X:
    #images.add(x*x-1)
    images.add(xplus1(x))
print(images)

print('f set ={',end='')
for x in X:
    print('(',x,',',xplus1(x),'),',end='')
    plt.scatter([x],[xplus1(x)])
print('}')

plt.show()
#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()