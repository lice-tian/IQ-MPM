import taichi as ti

@ti.data_oriented
class Params:
    def __init__(self) -> None:
        self.res = (512, 512)       # window resolution (width, height)
        self.max_fps = 120          # max FPS
        self.window_pos = (100, 100)    # window position
        self.enable_vsync = True    # vertical sync
        
        self.dt = 2e-4      # time step of simulation
        
        self.method = 'mpm' # mpm method, i.e, mpm, mls, iq
        self.dim = 2        # simulation dimension, 2 or 3

        self.grid_no = 128  # number of grids per axis
        self.grid_len = 1   # length of grids per axis

        self.particle_no = 8196     # number of particles
        self.particle_rho = 1       # 'ρ', particle density
        self.particle_r = self.grid_len / self.grid_no * 0.5    # particle radius
     

params = Params()