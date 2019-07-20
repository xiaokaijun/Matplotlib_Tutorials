import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

"""
在pycharm中figure窗口会出现3D图像无法拖动的情况。
解决办法如下：
    1. 依次打开 ： File | Settings | Tools | Python Scientific
    2. 将 show plots in tool window 前面的勾去掉
    3. 重新执行代码，即可在一个独立的窗口中显示画面
"""

#
# fig = plt.figure()
# ax = Axes3D(fig)
# # X, Y value
# X = np.arange(-4, 4, 0.25)
# Y = np.arange(-4, 4, 0.25)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X ** 2 + Y ** 2)
# # height value
# Z = np.sin(R)
#
# ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
# """
# ============= ================================================
#         Argument      Description
#         ============= ================================================
#         *X*, *Y*, *Z* Data values as 2D arrays
#         *rstride*     Array row stride (step size), defaults to 10
#         *cstride*     Array column stride (step size), defaults to 10
#         *color*       Color of the surface patches
#         *cmap*        A colormap for the surface patches.
#         *facecolors*  Face colors for the individual patches
#         *norm*        An instance of Normalize to map values to colors
#         *vmin*        Minimum value to map
#         *vmax*        Maximum value to map
#         *shade*       Whether to shade the facecolors
#         ============= ================================================
# """
#
# # I think this is different from plt12_contours
# ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.get_cmap('rainbow'))
# """
# ==========  ================================================
#         Argument    Description
#         ==========  ================================================
#         *X*, *Y*,   Data values as numpy.arrays
#         *Z*
#         *zdir*      The direction to use: x, y or z (default)
#         *offset*    If specified plot a projection of the filled contour
#                     on this position in plane normal to zdir
#         ==========  ================================================
# """
#
# ax.set_zlim(-2, 2)
#
# plt.show()

# 导入支持3D的模块
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

# 创建一个绘制的画布
fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z,rstride=1, cstride=1, cmap=cm.rainbow,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(-2, 2)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()






