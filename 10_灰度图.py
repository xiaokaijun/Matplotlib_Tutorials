import matplotlib.pyplot as plt;
import numpy as np;

a = np.array([130, 120,100,100,
              100,100,100,50,
              90,70,50,30,
              50,40,30,20]).reshape(4,4)


plt.imshow(a, interpolation='nearest', cmap='bone', origin='upper')
plt.colorbar(shrink=.92)

plt.xticks(())
plt.yticks(())
plt.show()