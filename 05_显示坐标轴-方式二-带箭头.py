import matplotlib.pyplot as plt;
import numpy as np;
import mpl_toolkits.axisartist as axisartist
"""
  构建一条y = sin(x) 的曲线
  构建一条y = cos(x)的曲线
"""

fig = plt.figure();

ax = axisartist.Subplot(fig,1,1,1);
fig.add_axes(ax);

# 隐藏所有边框
ax.axis[:].set_visible(False);
#                                1.第1个0表示x轴， 2.第2个0表示位置
ax.axis["x"] = ax.new_floating_axis(0,0);
ax.axis["x"].set_axis_direction("bottom");
ax.axis["x"].set_axisline_style("->",size=2.0)

ax.axis["y"] = ax.new_floating_axis(1,0);
ax.axis["y"].set_axis_direction("left");
ax.axis["y"].set_axisline_style("->",size=2.0)


# 设置X轴的标记
plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],
           [r"$-\pi$",r"$-\pi/2$","0","$\pi/2$","$\pi$"]);
plt.yticks(np.linspace(-1,1,5));


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





# 显示
plt.show();
