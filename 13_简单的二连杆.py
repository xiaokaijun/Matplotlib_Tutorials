import matplotlib.pyplot as plt
import numpy as np

# 定义函数计算末端坐标的位置
def compute_arm_config(link1_length, link2_length, joint1_angle, joint2_angle):
    # 计算关节2的坐标，也就是P2点的坐标
    joint1_x = link1_length*np.cos(joint1_angle)
    joint1_y = link2_length*np.sin(joint1_angle)
    joint2_x = joint1_x + link2_length*np.cos(joint1_angle+joint2_angle);
    joint2_y = joint1_y + link2_length*np.sin(joint1_angle+joint2_angle);
    return joint1_x, joint1_y, joint2_x, joint2_y

# 随机生成连杆1的长度
link1_length = np.random.random() * 30 + 20
# 随机生成连杆2的长度
link2_length = np.random.random() * 30 + 20
# 关节1旋转一定的角度
joint1_angle = np.random.random() * 2 * np.pi
# 关节2旋转一定的角度
joint2_angle = np.random.random() * 2 * np.pi

# 已知连杆的长度，以及两个关节旋转的角度 计算出末端的位置
joint1_x, joint1_y, joint2_x, joint2_y = compute_arm_config(link1_length, link2_length, joint1_angle, joint2_angle)

print("joint0_angle =", round(joint1_angle * 180 / np.pi, 1), "degrees")
print("joint1_angle =", round(joint2_angle * 180 / np.pi, 1), "degrees")
print("End Effector at x =", round(joint2_x, 1), "y =", round(joint2_x, 1))

# 基坐标
base_x = 0
base_y = 0

# 绘制坐标图像
# Plot the links
plt.plot([base_x, joint1_x, joint2_x], [base_y, joint1_y, joint2_y])
# Plot the base as a blue square  绘制基
plt.plot(base_x, base_y, 'bs', markersize=15, label='Base')
# Plot Joint-1 as a red circle  绘制关节1
plt.plot(joint1_x, joint1_y, 'ro', markersize=15, label='Joint-1')
# Plot End Effector as a green triangle 绘制末端
plt.plot(joint2_x, joint2_y, 'g^', markersize=15, label='End Effector')
plt.xlim(-100, 100)
plt.ylim(-100, 100)
plt.legend(fontsize=15)
plt.show()