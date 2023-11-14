import numpy as np
import matplotlib.pyplot as plt

def generate_uniform_particles(num_particles, radius, density_factor=2):
    # 生成均匀分布的角度
    theta = np.linspace(0, 2*np.pi, num_particles)

    # 将极坐标转换为笛卡尔坐标
    x_outer = radius * np.cos(theta)
    y_outer = radius * np.sin(theta)

    # 添加更多粒子到圆形内部
    x_inner = np.random.uniform(low=-radius, high=radius, size=int(num_particles * density_factor))
    y_inner = np.random.uniform(low=-radius, high=radius, size=int(num_particles * density_factor))

    # 合并内外部的粒子
    x = np.concatenate([x_outer, x_inner])
    y = np.concatenate([y_outer, y_inner])

    # 创建粒子数组
    particles = np.column_stack((x, y))

    return particles

# 圆形的半径
circle_radius = 1.0

# 生成均匀分布的粒子在圆形内部
num_particles = 500
particles = generate_uniform_particles(num_particles, circle_radius)

# 绘制圆形
circle = plt.Circle((0, 0), circle_radius, edgecolor='black', facecolor='none')
fig, ax = plt.subplots(figsize=(6, 6))
ax.add_patch(circle)

# 绘制粒子
plt.scatter(particles[:, 0], particles[:, 1], color='blue', s=5)
plt.title('Particles in and around a 2D Circle')
plt.axis('equal')
plt.show()
