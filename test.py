import taichi as ti
import numpy as np

# initialize 'cuda' backend & set default 'int' and 'float'
ti.init(arch=ti.cuda, default_ip=ti.i32, default_fp=ti.f32)

model_path = 'mesh2particle/bunny_res0_step0.01.npy'
model = np.load(model_path).astype(np.float32)

n_particles = model.shape[0]
n_grid = 128

dx, inv_dx = 1 / n_grid, float(n_grid)

dt = 1e-4

# particle properties
x = ti.Vector.field(2, dtype=float, shape=n_particles)  # position
v = ti.Vector.field(2, dtype=float, shape=n_particles)  # velocity
F = ti.Matrix.field(2, 2, dtype=float, shape=n_particles)   # deformation gradient
C = ti.Matrix.field(2, 2, dtype=float, shape=n_particles)   # affine velocity field

grid_v = ti.Vector.field(2, dtype=float, shape=(n_grid, n_grid))  # grid node momentum/velocity
grid_m = ti.field(dtype=float, shape=(n_grid, n_grid))  # grid node mass


@ti.kernel
def initialize(model: ti.types.ndarray()):
    for i in range(n_particles):
        x[i] = [model[i, 0] * 0.4 + 0.3, 
                model[i, 1] * 0.4 + 0.3]
        v[i] = ti.Matrix.zero(dt=float, n=2)
        F[i] = ti.Matrix.identity(dt=float, n=2)
        C[i] = ti.Matrix.zero(dt=float, n=2, m=2)


@ti.kernel
def substep():
    for i, j in grid_m:
        grid_v = [0, 0]
        grid_m = 0

    # Particle state update and scatter to grid (P2G)
    for p in x:
        # deformation update
        F[p] = (ti.Matrix.identity(float, 2) + dt * C[p]) @ F[p]

        # grid momentum
        base = (x[p] * inv_dx - 0.5).cast(int)
        print(base)


initialize(model=model)
gui = ti.GUI("test", res=512, background_color=0x112F41)
while not gui.get_event(ti.GUI.ESCAPE, ti.GUI.EXIT):
    gui.circles(
            x.to_numpy(),
            radius=1.0,
            color=0xED553B
        )
    gui.show()