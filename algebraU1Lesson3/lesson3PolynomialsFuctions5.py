#Three lines to make our compiler able to draw:
import sys
import math
import matplotlib.pyplot as plt

# X={-1,0,1}
# Y={0,-1,-2}
# X=range(0,5)
# X={2,4,6,8}
# Y={1,2,3,4,5,6}
X={1,0,-2,0.5,math.sqrt(5),2*math.sqrt(2)+1,1-math.sqrt(2)}


def fn(x):
    # return x*x-1
    # return x+1
    # return x*0.5 
    return x*x-(2*x)+5

# 1-get the projections or range
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