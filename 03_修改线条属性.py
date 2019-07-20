import matplotlib.pyplot as plt;
import numpy as np;
"""
  构建一条y = sin(x) 的曲线
"""

# 构建X方向的值, 1.初始值 2.结束值 3.分成多少份
X = np.linspace(-np.pi,np.pi,100,endpoint=True);
# 构建Y方向的值
SY = np.sin(X);
CY = np.cos(X);

# 绘制直线, X ,Y 的坐标点
plt.plot(X,SY,color="red",linewidth=2.0);
plt.plot(X,CY,color="blue",linewidth=2.0,linestyle="-");

# 设置x,y的上下限
plt.xlim(-4,4);
plt.ylim(-1,1);

# 设置X轴的标记
plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],
           [r"$-\pi$",r"$-\pi/2$","0","$\pi/2$","$\pi$"]);
plt.yticks(np.linspace(-1,1,5));

# 显示
plt.show();
