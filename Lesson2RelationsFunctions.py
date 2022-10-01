#Three lines to make our compiler able to draw:
import sys

import matplotlib.pyplot as plt

#X={1,2,3}
#Y={1,2,3}
X=range(1,10)
Y=range(-10,10)
#a R b y=x
for x in X:
  for y in Y:
    #if x + y==10:
    #if x == y:
    #if x==abs(y):
    if x==0.5*y:
      plt.scatter([x],[y])
  
plt.show()
#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()