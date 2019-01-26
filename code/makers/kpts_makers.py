import numpy as np
import sys

def make_auto_kpts(filename, grid = [11,11,11, 0,0,0]):
    
    f = open(filename, 'w+')
    f.write('K_POINTS   automatic\n')
    f.write('    ' + str(grid[0]) + ' ' + str(grid[1]) + ' ' + str(grid[2]) + ' ' + str(grid[3]) + ' ' + str(grid[4]) + ' ' + str(grid[5]) + ' \n')
    f.close()

if __name__ == "__main__":
    filename = sys.argv[1]
    make_auto_kpts(filename)

