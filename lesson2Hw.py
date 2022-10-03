#Three lines to make our compiler able to draw:
import sys

import matplotlib.pyplot as plt

X={1,2,3,6,11}
Y={1,2,3,6,11}
#a R b y=x
for x in X:
  for y in Y:
    if (x+(2*y))%2 ==1:
      plt.scatter([x],[y])
  
plt.show()
#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()