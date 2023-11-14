import taichi as ti
from config import params

@ti.data_oriented
class Particles:
    def __init__(self) -> None:
        self.vol = params.particle_r ** params.dim  # particle approximate volume
        self.m = params.particle_rho * self.vol     # particle mass

        self.pos = ti.Vector.field(n=params.dim, dtype=float, shape=params.particle_no) # position of particles
        self.v = ti.Vector.field(n=params.dim, dtype=float, shape=params.particle_no)   # velocity of particles