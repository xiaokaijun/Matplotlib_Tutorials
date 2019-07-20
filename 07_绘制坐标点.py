import matplotlib.pyplot as plt;
import numpy as np;
"""
  绘制一系列坐标点
"""

# 构建X方向的值, 1.初始值 2.结束值 3.分成多少份
X = np.linspace(-5,5,10);
# 构建Y方向的值
Y = 2*X + 1;

# 绘制坐标点, X ,Y 的坐标点
plt.scatter(X,Y);

# 显示
plt.show();
