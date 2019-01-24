import numpy as np
import sys 

def make_bulk_Sb2Te3_struc(struc_filename, a = 4.38, c = 30.5, mu = 0.212000, nu =0.400000):

    # #Lattice vectors (Rhombohedral)
    v1 = [-0.5*a, -0.5*a/np.sqrt(3) ,c/3]
    v2 = [0.5*a, -0.5*a/np.sqrt(3), c/3]
    v3 = [0, a/np.sqrt(3), c/3]
    
    f = open(struc_filename, 'w+')

    f.write('    ibrav = 0,\n')
    f.write('    nat = 5, ntyp = 2\n')
    f.write('/\n')
    
    f.write('ATOMIC_SPECIES\n')
    f.write('Sb 121.760 Bi.rel-pbe-dn-kjpaw_psl.1.0.0.UPF\n')
    f.write('Te 127.600 Te.rel-pbe-dn-kjpaw_psl.1.0.0.UPF\n')
    f.write('\n')
    
    f.write('CELL_PARAMETERS (angstrom)\n')
    f.write('  ' +str(v1[0]) + '  ' + str(v1[1]) + '  ' + str(v1[2])+ '\n')
    f.write('   ' +str(v2[0]) + '  ' + str(v2[1]) + '  ' + str(v2[2])+ '\n')
    f.write('   0.000000'+ '  ' + str(v3[1]) + '  ' + str(v3[2])+ '\n')
    f.write('\n')

    f.write('ATOMIC_POSITIONS (crystal)\n')
    f.write('Sb  ' + str(-nu) + '  ' +str(-nu) + '  ' +str(-nu)+ '\n')
    f.write('Te  ' + str(-mu) + '  ' +str(-mu) + '  ' +str(-mu)+'\n')
    f.write('Te  ' + str(0.000) + '  ' +str(0.000) + '  ' +str(0.000)+'\n')
    f.write('Te  ' + str(mu) + '  ' +str(mu) + '  ' +str(mu)+'\n')
    f.write('Sb  ' + str(nu) + '  ' +str(nu) + '  ' +str(nu)+'\n')
    
    f.close()

if __name__ == "__main__":
    filename = sys.argv[1]
    make_bulk_Sb2Te3_struc(filename)
