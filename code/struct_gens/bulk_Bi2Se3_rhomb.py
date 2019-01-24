import numpy as np
import sys 

def make_bulk_Bi2Se3_struc(struc_filename, a = 4.125, c = 28.00000, mu = 0.211000, nu =0.400000):
    
    #Lattice vectors (Rhombohedral)
    v1 = [-0.5*a, -0.5*a/np.sqrt(3) ,c/3]
    v2 = [0.5*a, -0.5*a/np.sqrt(3), c/3]
    v3 = [0, a/np.sqrt(3), c/3]
    
    f = open(struc_filename, 'w+')

    f.write('    ibrav = 0,\n')
    f.write('    nat = 5, ntyp = 2\n')
    f.write('/\n')
    
    f.write('ATOMIC_SPECIES\n')
    f.write('Bi 208.9804 Bi.rel-pbe-dn-kjpaw_psl.1.0.0.UPF\n')
    f.write('Se 78.9600  Se.rel-pbe-dn-kjpaw_psl.1.0.0.UPF\n')
    f.write('\n')
    
    f.write('CELL_PARAMETERS (angstrom)\n')
    f.write('  ' +str(v1[0]) + '  ' + str(v1[1]) + '  ' + str(v1[2])+ '\n')
    f.write('   ' +str(v2[0]) + '  ' + str(v2[1]) + '  ' + str(v2[2])+ '\n')
    f.write('   0.000000'+ '  ' + str(v3[1]) + '  ' + str(v3[2])+ '\n')
    f.write('\n')

    f.write('ATOMIC_POSITIONS (crystal)\n')
    f.write('Bi  ' + str(-nu) + '  ' +str(-nu) + '  ' +str(-nu)+ '\n')
    f.write('Se  ' + str(-mu) + '  ' +str(-mu) + '  ' +str(-mu)+'\n')
    f.write('Se  ' + str(0.000) + '  ' +str(0.000) + '  ' +str(0.000)+'\n')
    f.write('Se  ' + str(mu) + '  ' +str(mu) + '  ' +str(mu)+'\n')
    f.write('Bi  ' + str(nu) + '  ' +str(nu) + '  ' +str(nu)+'\n')
    
    f.close()

if __name__ == "__main__":
    filename = sys.argv[1]
    make_bulk_Bi2Se3_struc(filename)
