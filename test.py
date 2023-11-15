import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon

def generate_points_in_shape(radius, shape_vertices, resolution):
    shape = Polygon(shape_vertices)
    min_x, min_y, max_x, max_y = shape.bounds
    points = []

    # 定义网格的步长
    step = radius * 2 / resolution

    # 生成网格点
    for x in np.arange(min_x, max_x, step):
        for y in np.arange(min_y, max_y, step):
            point = Point(x, y)
            
            if shape.contains(point):
                points.append((x, y))

    return np.array(points)

def plot_points(x, y, radius, shape_vertices):
    plt.scatter(x, y, s=5, c='blue', alpha=0.7)
    plt.gca().set_aspect('equal', adjustable='box')  # 保持坐标轴的纵横比一致
    plt.xlabel('X')
    plt.ylabel('Y')
    
    # 绘制物体的轮廓
    shape = Polygon(shape_vertices)
    x, y = shape.exterior.xy
    plt.plot(x, y, color='red', linewidth=2, linestyle='-', alpha=0.7)

    # 绘制粒子的半径
    for xi, yi in zip(x, y):
        circle = plt.Circle((xi, yi), radius, color='green', fill=False, linestyle='--', linewidth=1)
        plt.gca().add_patch(circle)

    plt.title('Points Generated with Radius in a Shape')
    plt.show()

# 定义一个任意形状的物体（这里使用一个五边形作为示例）
shape_vertices = [(2, 0), (4, 1), (5, 3), (3, 5), (1, 3)]

# 定义粒子的半径
particle_radius = 0.1

# 定义网格分辨率
grid_resolution = 2

# 生成在物体内的粒子坐标
points = generate_points_in_shape(particle_radius, shape_vertices, grid_resolution)
x, y = points[:, 0], points[:, 1]

# 绘制粒子分布和物体轮廓
plot_points(x, y, particle_radius, shape_vertices)
