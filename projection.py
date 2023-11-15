import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import tripy

def read_ply(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    vertex_start = lines.index('end_header\n') + 1
    vertices = np.array([list(map(float, line.split()[:3])) for line in lines[vertex_start:]])

    return vertices

def project_3d_to_2d(vertices, axis_to_project):
    return vertices[:, [0, 1]]

def plot_2d_projection(vertices_2d, triangles):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    for triangle_indices in triangles:
        triangle_indices = np.array(triangle_indices, dtype=int)
        triangle = vertices_2d[triangle_indices + (triangle_indices[0],)]  # 封闭三角形

        poly = Polygon(triangle, edgecolor='black', facecolor='none')
        ax.add_patch(poly)

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('2D Projection of Stanford Bunny')

    plt.axis('scaled')  # 设置坐标轴比例一致
    plt.show()

def main():
    # 读取 Stanford Bunny 模型
    bunny_vertices = read_ply('bun_zipper_res4.ply')  # 使用你下载的文件

    # 选择一个坐标轴进行投影（这里选择 Z 轴）
    axis_to_project = 2

    # 投影到二维平面
    bunny_2d = project_3d_to_2d(bunny_vertices, axis_to_project)

    # 从三维模型中获取三角形
    bunny_triangles = tripy.earclip(bunny_2d)

    # 绘制二维投影
    plot_2d_projection(bunny_2d, bunny_triangles)

if __name__ == "__main__":
    main()
