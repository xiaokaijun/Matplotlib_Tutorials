import matplotlib.pyplot as plt;
import numpy as np;
"""
  绘制散点图
"""

# 定义绘制点的数量
n = 1024

# X 方向上的值
X = np.random.normal(0,1,n);
print(X)
Y = np.random.normal(0,1,n);

T = np.arctan2(Y,X)
print(T)
# 绘制坐标点, X ,Y 的坐标点
plt.scatter(X,Y,c=T,alpha=0.5);

# 设置x的值的范围
plt.xlim(-1.5,1.5)
# 隐藏x的坐标值
plt.xticks(())

# 设置y值的范围
plt.ylim(-1.5,1.5)


# 显示
plt.show();
