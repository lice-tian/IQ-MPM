import taichi as ti
import argparse
from config import params

# initialize 'cuda' backend & set default 'int' and 'float'
ti.init(arch=ti.cuda, default_ip=ti.i32, default_fp=ti.f32)

# parse arguments
parser = argparse.ArgumentParser(description='')
parser.add_argument('-m', '-method', 
                    dest='method',
                    type=str, 
                    default='mpm',
                    help='Specify the mpm method: mpm, mls, iq')
parser.add_argument('-d', '-dim',
                    dest='dim',
                    type=int,                    
                    default=2,
                    help='Specify the simulation dimension')
args = parser.parse_args()

# initialize 'params' before creating grid and particle objects
params.method = args.method
params.dim = args.dim

# initialize window
window = ti.ui.Window(name=params.method, res=params.res, vsync=params.enable_vsync, fps_limit=params.max_fps, pos=params.window_pos)
canvas = window.get_canvas()

# physics computing and rendering
while window.running:
    canvas.set_background_color((0.067, 0.184, 0.255))
    window.show()