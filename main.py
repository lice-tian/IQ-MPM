import taichi as ti
import argparse

# initialize backend
ti.init(arch=ti.cuda)

# set default 'int' and 'float'
ti.init(default_ip=ti.i32, default_fp=ti.f32)

# parse arguments
parser = argparse.ArgumentParser(description='')
parser.add_argument('-m', '-method', 
                    dest='method',
                    type=str, 
                    default='mls',
                    help='Specify the mpm method: mpm, mls, iq')
parser.add_argument('-d', '-dim',
                    dest='dim',
                    type=int,                    
                    default=2,
                    help='Specify the simulation dimension')
args = parser.parse_args()

print(args.method)

