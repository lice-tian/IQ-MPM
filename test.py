import taichi as ti
import numpy as np

# initialize 'cuda' backend & set default 'int' and 'float'
ti.init(arch=ti.cuda, default_ip=ti.i32, default_fp=ti.f32)

model_path = 'mesh2particle/bunny_res0_step0.01.npy'
model = np.load(model_path).astype(np.float32)

n_particles = model.shape[0]
n_grid = 128

dx, inv_dx = 1 / n_grid, float(n_grid)

x = ti.Vector.field(2, dtype=float, shape=n_particles)  # particle position

@ti.kernel
def initialize(model: ti.types.ndarray()):
    for i in range(n_particles):
        x[i] = [model[i, 0] * 0.5 + 0.25, 
                model[i, 1] * 0.5 + 0.25]


initialize(model=model)
gui = ti.GUI("test", res=512, background_color=0x112F41)
while not gui.get_event(ti.GUI.ESCAPE, ti.GUI.EXIT):
    gui.circles(
            x.to_numpy(),
            radius=1.5,
            color=0xED553B
        )
    gui.show()