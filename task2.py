import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(20)
y = np.random.rand(20)
print(x, y)

plt.scatter(x, y, color="cyan")
plt.xlabel("ось x")
plt.ylabel("ось y")
plt.title("диаграмма рассеяния для случайных чисел")
plt.grid(True)
plt.show()