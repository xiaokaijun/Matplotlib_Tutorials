import matplotlib.pyplot as plt;
import numpy as np;
"""
  构建一条y = sin(x) 的曲线
"""

# 构建X方向的值, 1.初始值 2.结束值 3.分成多少份
X = np.linspace(-2*np.pi,2*np.pi);
# 构建Y方向的值
Y = np.sin(X);

# 绘制直线, X ,Y 的坐标点
plt.plot(X,Y);

# 显示
plt.show();
