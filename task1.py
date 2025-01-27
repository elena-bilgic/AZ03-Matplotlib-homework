import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(0, 1, 1000)

plt.hist(data, bins=7, color="magenta")

plt.xlabel("значение")
plt.ylabel("частота")
plt.title("гистограмма случайных чисел с нормальным распределением")
plt.grid(axis='y', alpha=0.75)
plt.show()
