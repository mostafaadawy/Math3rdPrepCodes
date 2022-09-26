print ('lets draw')
import matplotlib.pyplot as plt
import numpy as np

# xpoints = np.array([1,2,3,4,5,6,7,8,9,0])
# ypoints = np.array([11,12,13,14,15,16,17,18,19,20])
X={1,2,3,4,4}
Y={1,2,3,4}
print(X)
#X = np.array(range(1,20))
#Y = np.array(range(20,40))
for x in X:
    for y in Y:
        plt.scatter([x],[y])
plt.show()

