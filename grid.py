import taichi as ti
from config import params

@ti.data_oriented
class Grid:
    def __init__(self) -> None:
        self.size = (params.grid_no,) * params.dim      # grid size of all axes
        self.cell_len = params.grid_len / params.grid_no    # length of every cell

        self.m = ti.field(dtype=float, shape=self.size)     # mass of cells
        self.v = ti.Vector.field(n=params.dim, dtype=float, shape=self.size)    # velocity of cells
        