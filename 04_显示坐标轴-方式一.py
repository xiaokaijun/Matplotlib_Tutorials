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
plt.ylim(-1.2,1.2);

# 设置X轴的标记
plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],
           [r"$-\pi$",r"$-\pi/2$","0","$\pi/2$","$\pi$"]);
plt.yticks(np.linspace(-1,1,5));

ax = plt.gca();
ax.spines["right"].set_color("none");
ax.spines["top"].set_color("none");

ax.xaxis.set_ticks_position("bottom")
ax.spines["bottom"].set_position(("data",0));

ax.yaxis.set_ticks_position("left")
ax.spines["left"].set_position(("data",0));

#  设置坐标轴的说明， 默认情况下不支持中文
plt.xlabel("this is x value")
plt.ylabel("this is y value")
plt.title("x,y tutorials")

# 显示
plt.show();
