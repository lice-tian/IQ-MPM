import numpy as np
from plyfile import PlyData
import matplotlib.pyplot as plt

def addLine(p0, p1, lines):
    global count
    if (p0, p1) in lines or (p1, p0) in lines:
        return
    else:
        lines.append((p0, p1))


def getLines(faces):
    lines = []
    for face in faces:
        face = face[0] # before changing, 'face' is like '(array([164,  94,  98]),)'
        addLine(face[0], face[1], lines)
        addLine(face[0], face[2], lines)
        addLine(face[1], face[2], lines)
    return np.array(lines)


ply_path = 'bun_zipper_res4.ply'
ply_data = PlyData.read(ply_path)

vertices = ply_data.elements[0][:] # 'vertex' element content: (x, y, z, confidence, intensity)
faces = ply_data.elements[1][:]    # 'face' element content: (index0, index1, index2)

lines = getLines(faces)

# # 读取PLY文件
# def read_ply_file(file_path):
#     with open(file_path, 'rb') as f:
#         plydata = PlyData.read(f)
#     return plydata

# # 获取二维投影的边缘
# def get_2d_projection_edges(vertices):
#     # 投影到xoy平面
#     projected_vertices = vertices[:, [0, 1]]

#     # 计算凸包
#     hull = ConvexHull(projected_vertices)

#     # 获取凸包的边缘点
#     boundary_points = projected_vertices[hull.vertices]

#     return boundary_points

# # 绘制边缘
# def plot_edges(boundary_points):
#     plt.plot(boundary_points[:, 0], boundary_points[:, 1], 'r-')
#     plt.scatter(boundary_points[:, 0], boundary_points[:, 1], c='b', marker='o')
#     plt.xlabel('X')
#     plt.ylabel('Y')
#     plt.title('2D Projection Edges')
#     plt.show()

# # 主程序
# if __name__ == "__main__":
#     # 请替换为你的PLY文件路径
#     ply_file_path = 'bun_zipper_res4.ply'

#     # 读取PLY文件
#     ply_data = read_ply_file(ply_file_path)

#     # 获取顶点坐标
#     vertices = np.vstack([ply_data['vertex']['x'], ply_data['vertex']['y'], ply_data['vertex']['z']]).T

#     # 获取二维投影的边缘
#     boundary_points = get_2d_projection_edges(vertices)

#     # 绘制边缘
#     plot_edges(boundary_points)