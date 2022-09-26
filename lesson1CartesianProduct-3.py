# code for online course
#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

X = np.array(range(1,10))
Y = np.array(range(1,10))
for x in X:
  for y in Y:
    plt.scatter([x], [y])

plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()