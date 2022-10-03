#Three lines to make our compiler able to draw:
import sys
import math
import matplotlib.pyplot as plt


X=range(-5,5)


def threexminus3(x):
    return 3*x-3

# 1-get the projections or range
images=set()
for x in X:
    #images.add(x*x-1)
    images.add(threexminus3(x))
print('range',images)

print('f set ={',end='')
for x in X:
    print('(',x,',',threexminus3(x),'),',end='')
    plt.scatter([x],[threexminus3(x)])
print('}')

plt.show()
#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()