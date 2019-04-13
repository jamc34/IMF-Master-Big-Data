import numpy as np
import matplotlib.pyplot as plt

y = np.random.rand(1000000)
y*100
plt.hist(y,100)
plt.axis()
plt.show()
