import numpy as np
import sys 

def make_bulk_NaCl(struc_filename, a = 5.6402):
    
    v1 = [0, a/2, a/2]
    v2 = [a/2, 0, a/2]
    v3 = [a/2, a/2, 0]
    
    f = open(struc_filename, 'w+')
    
    f.write('ATOMIC_SPECIES\n')
    f.write('Na 22.98798 Na.pbe-n-kjpaw_psl.1.0.0.UPF\n')
    f.write('Cl 35.45300 Cl.pbesol-spn-kjpaw_psl.1.0.0.UPF\n')
    f.write('\n')
    
    f.write('CELL_PARAMETERS (angstrom)\n')
    f.write('   ' +str(v1[0]) + '  ' + str(v1[1]) + '  ' + str(v1[2])+ '\n')
    f.write('   ' +str(v2[0]) + '  ' + str(v2[1]) + '  ' + str(v2[2])+ '\n')
    f.write('   ' +str(v3[0]) + '   ' +str(v2[1])+  '   ' + str(v3[2])+ '\n')
    f.write('\n')

    f.write('ATOMIC_POSITIONS (crystal)\n')
    f.write('Na   0.0000000  0.0000000 0.0000000\n')
    f.write('Cl   0.5000000  0.5000000 0.5000000\n')

    f.close()


if __name__ == "__main__":
    filename = sys.argv[1]
    make_bulk_NaCl(filename)
