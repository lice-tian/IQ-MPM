import numpy as np
from plyfile import PlyData

class PlyParser:
    def __init__(self, file_path: str) -> None:
        ply_data = PlyData.read(file_path)

        # 'vertex' element content: (x, y, z, confidence, intensity)
        self.vertices = np.array([(v[0], v[1]) for v in ply_data['vertex']])
        
        # normalize vertices by larger diff
        min_v = np.min(self.vertices, axis=0)  # 'axis': 0 is col, 1 is row, None is all
        max_v = np.max(self.vertices, axis=0)
        diff = max_v - min_v
        if(diff[0] > diff[1]):
            self.vertices = (self.vertices - min_v) / diff[0]
            self.__min_x = 0
            self.__max_x = 1
            self.__min_y = 0
            self.__max_y = diff[1] / diff[0]
        else:
            self.vertices = (self.vertices - min_v) / diff[1]
            self.__min_x = 0
            self.__max_x = diff[0] / diff[1]
            self.__min_y = 0
            self.__max_y = 1
        
        # 'face' element content: '(array([index0, index1, index2]),)'
        self.faces = np.array([f[0] for f in ply_data['face']])
    
    # compute cross of point and edge of triangle(face)
    def __cross(self, p0, p1, p2) -> float:
        return (p0[0] - p2[0]) * (p1[1] - p2[1]) - (p1[0] - p2[0]) * (p0[1] - p2[1])

    # judge whether point is inside trangle or not
    def __isPointInTriangle(self, point, triangle) -> bool:
        sign0 = self.__cross(point, triangle[0], triangle[1])
        sign1 = self.__cross(point, triangle[1], triangle[2])
        sign2 = self.__cross(point, triangle[2], triangle[0])

        has_neg = (sign0 < 0) or (sign1 < 0) or (sign2 < 0)
        has_pos = (sign0 > 0) or (sign1 > 0) or (sign2 > 0)

        # if all cross are negetive or positive, point is inside triangle
        return not (has_neg and has_pos)

    # generate particles by 'step', step in (0, 1)
    def toParticles(self, step) -> np.ndarray:
        particles = []
        for x in np.arange(self.__min_x, self.__max_x, step):
            for y in np.arange(self.__min_y, self.__max_y, step):
                print("Processing({}, {})".format(x, y))
                for f in self.faces:
                    triangle = [self.vertices[index] for index in f]
                    if self.__isPointInTriangle((x,y), triangle):
                        particles.append((x, y))
                        break
        return np.array(particles)

if __name__ == '__main__':

    import matplotlib.pyplot as plt
    import os

    ply_path = 'bun_zipper.ply'
    out_file = 'bunny_res0_step0.01.npy'
    
    if os.path.exists(out_file):
        particles = np.load(out_file)
    else:
        print("Reading ply file: " + ply_path)
        parser = PlyParser(ply_path)
        print("Converting to particles")
        particles = parser.toParticles(0.01)
        print("Saving particles")
        np.save(out_file, particles)

    for p in particles:
        circle = plt.Circle(p, 0.005, color='green', fill=False, linestyle='--', linewidth=1)
        plt.gca().add_patch(circle)
    plt.title('Bunny Particles')
    plt.show()
