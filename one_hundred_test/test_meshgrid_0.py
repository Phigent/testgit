import numpy as np
import matplotlib.pyplot as plt

nx, ny = (5, 3)
#创建一位数组x
x = np.linspace(0, 1, nx)
print(x)

#创建一位数组y
y =  np.linspace(0, 1, ny)
print(y)

xv, yv, = np.meshgrid(x, y)
print(xv)
print(yv)

plt.scatter(xv.flatten(), yv.flatten(), c='red')
plt.xticks(ticks = x)
plt.yticks(ticks = y)
plt.show()
