import numpy as np
import sys 

def make_Sb2Te3_QL_struc(struc_filename, a = 4.38, c = 30.1, D1 = 1, D2 = 1.5):
    c = vac_layer + 2*D1 + 2*D2
    IL1 = D1/c
    IL2 = D2/c
    
    #Lattice vectors (Hexagonal)
    v1 = [a, 0, 0]
    v2 = [-0.5*a, 0.5*np.sqrt(3)*a, 0]
    v3 = [0, 0, c]
    
    f = open(struc_filename, 'w+')

    f.write('    ibrav = 0,\n')
    f.write('    nat = 5, ntyp = 2\n')
    f.write('/\n')
    
    f.write('ATOMIC_SPECIES\n')
    f.write('Sb 121.760 Sb.rel-pbe-dn-kjpaw_psl.1.0.0.UPF\n')
    f.write('Te 127.600 Te.rel-pbe-dn-kjpaw_psl.1.0.0.UPF\n')
    f.write('\n')
    
    f.write('CELL_PARAMETERS (angstrom)\n')
    f.write('  ' +str(v1[0]) + '  ' + str(v1[1]) + '  ' + str(v1[2])+ '\n')
    f.write('   ' +str(v2[0]) + '  ' + str(v2[1]) + '  ' + str(v2[2])+ '\n')
    f.write('   0.000000'+ '  0.000000' + '  ' + str(v3[2])+ '\n')
    f.write('\n')

    f.write('ATOMIC_POSITIONS (crystal)\n')
    f.write('Te  0.0000000  0.0000000 0.0000000\n')
    f.write('Sb  0.6666667  0.3333333 ' +str(IL1) +'\n')
    f.write('Te  0.3333333  0.6666667 ' +str(IL1 +IL2) +'\n')
    f.write('Sb  0.0000000  0.0000000 ' +str(2*IL1 +IL2) +'\n')
    f.write('Te  0.6666667  0.3333333 ' +str(2*IL1 +2*IL2) +'\n')

    f.close()

if __name__ == "__main__":
    filename = sys.argv[1]
    make_Sb2Te3_QL_struc(filename)
