#Three lines to make our compiler able to draw:
import sys
import math
import matplotlib.pyplot as plt


X=range(-5,5)


def constantB0():
    return 0

def constantB3():
    return 3
def constantBve3():
    return -3


for x in X:
    plt.scatter([x],[constantB0()])
    plt.scatter([x],[constantB3()])
    plt.scatter([x],[constantBve3()])

plt.show()


#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()