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

# 绘制直线, X ,Y 的坐标点     # 增加图例显示
# 注意l1,后面的逗号，表示取列表中的第1个位置
l1,= plt.plot(X,SY,color="red",linewidth=2.0,label="sin(x)");
l2,= plt.plot(X,CY,color="blue",linewidth=2.0,linestyle="-" ,label="cos(x)");

"""
loc 取值： 
  best (默认)
	upper right
	upper left
	lower left
	lower right
	right
	center left
	center right
	lower center
	upper center
	center 
handles : 表示要处理哪些线
lables ： 需要与handles对应，表示线的说明
"""

# 调用方式一
# plt.legend(loc="upper left");
# 调用方式二
plt.legend(handles=[l1,l2],labels=["xixi","haha"],loc="best");

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
plt.title("x,y tutorials")


# 显示
plt.show();
