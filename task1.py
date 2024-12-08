import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(0, 1, 1000)

plt.hist(data, bins=6, color="hotpink")

plt.xlabel("ось x")
plt.ylabel("ось y")
plt.title("гистограмма для случайных чисел")
plt.show()
