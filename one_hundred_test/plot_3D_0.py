from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

#生成 X，Y,Z
x = np.arange(-5, 5, 0.25)
y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(x, y)  # x-y平面的网络
R = np.sqrt( X ** 2 + Y ** 2)

Z = np.sin(R)

print(Z)

#绘制3D曲面图
fig = plt.figure()
ax = Axes3D(fig)

plt.xticks(ticks=np.arange(-5,6))
ax.plot_surface(X, Y, Z, cmap=plt.get_cmap('rainbow'))
plt.show()
