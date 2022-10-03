#Three lines to make our compiler able to draw:
import sys

import matplotlib.pyplot as plt


X={2,4,6,8}
Y={1,2,3,4,5,6}

def halfx(x):
    return x*0.5

# 1-get the projections or range
images=set()
for x in X:
    #images.add(x*x-1)
    images.add(halfx(x))
print('range',images)

print('f set ={',end='')
for x in X:
    print('(',x,',',halfx(x),'),',end='')
    plt.scatter([x],[halfx(x)])
print('}')

plt.show()
#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()