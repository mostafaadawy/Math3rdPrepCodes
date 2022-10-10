#Three lines to make our compiler able to draw:
import sys

import matplotlib.pyplot as plt


X={-1,0,1}
Y={0,-1,-2}

def x2minusone(x):
    return x*x-1

# 1-get the projections or range
images=set()
for x in X:
    #images.add(x*x-1)
    images.add(x2minusone(x))
print('range =',images)

print('f set ={',end='')
for x in X:
    print('(',x,',',x2minusone(x),'),',end='')
    plt.scatter([x],[x2minusone(x)])
print('}')

plt.show()
#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()