#Three lines to make our compiler able to draw:
import sys
import math
import matplotlib.pyplot as plt


X=range(-5,5)



def constantBntve1():
    return -1
plt.title("constant function")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.plot([0], marker = '.')
plt.plot([-2], marker = '.')
for x in X:
    plt.scatter([x],[constantBntve1()],s=100)
plt.grid()
plt.show()


#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()