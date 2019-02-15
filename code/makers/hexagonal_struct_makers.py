import numpy as np
import sys 

def make_graphene(struc_filename, a = 2.460, vac_layer = 15):
    c = vac_layer + 2*D1 + 2*D2
    
    #Lattice vectors (Hexagonal)
    v1 = [a, 0, 0]
    v2 = [-0.5*a, 0.5*np.sqrt(3)*a, 0]
    v3 = [0, 0, c]
    
    f = open(struc_filename, 'w+')
    
    f.write('ATOMIC_SPECIES\n')
    f.write('C 12.0107 C.pbe-n-kjpaw_psl.1.0.0.UPF\n')
    f.write('\n')
    
    f.write('CELL_PARAMETERS (angstrom)\n')
    f.write('  ' +str(v1[0]) + '  ' + str(v1[1]) + '  ' + str(v1[2])+ '\n')
    f.write('   ' +str(v2[0]) + '  ' + str(v2[1]) + '  ' + str(v2[2])+ '\n')
    f.write('   0.000000'+ '  0.000000' + '  ' + str(v3[2])+ '\n')
    f.write('\n')

    f.write('ATOMIC_POSITIONS (crystal)\n')
    f.write('C  0.0000000  0.0000000 0.0000000\n')
    f.write('C  0.3333333  0.6666667 0.0000000\n')

    f.close()

if __name__ == "__main__":
    filename = sys.argv[1]
    make_graphene(filename)
