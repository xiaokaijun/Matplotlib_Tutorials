import matplotlib.pyplot as plt;
import numpy as np;

"""
  matplotlib官方教学教程网址：https://matplotlib.org/tutorials/index.html
  构建一条y = 2x + 1 的直线
"""

# 构建X方向的值, 1.初始值 2.结束值 3.分成多少份
X = np.linspace(-5,5,10);
# 构建Y方向的值
Y = 2*X + 1;

# 绘制直线, X ,Y 的坐标点
plt.plot(X,Y);

# 显示
plt.show();
