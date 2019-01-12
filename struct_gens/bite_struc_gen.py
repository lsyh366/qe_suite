import numpy as np
import os
import sys

inter_layer = float(sys.argv[1])

vacuum_layer = 16          #Thickness of vacuum layer (angstrom)

def two_ql_zred(inter, vacuum):

        xred = [0, 1.68, 3.70, 5.72, 7.40]
        xred.append(7.40 + inter)
        xred.append(9.08 + inter)
        xred.append(11.10 + inter)
        xred.append(13.12 + inter)
        xred.append(14.80 + inter)

        a = 4.383  #Lattice vector (angstroms)
        c = 14.80 + inter + vacuum
        xred = np.array(xred)
        xred = xred/c
        xred = xred.astype(str)
        return(c/a, xred)
    
    
    
(celldm3, xred) = two_ql_zred(inter_layer, vacuum_layer)

with open('2ql.in', 'r') as file:
	filedata = file.read()
	filedata = filedata.replace('ATPOS01', xred[0])
	filedata = filedata.replace('ATPOS02', xred[1])
	filedata = filedata.replace('ATPOS03', xred[2])
	filedata = filedata.replace('ATPOS04', xred[3])
	filedata = filedata.replace('ATPOS05', xred[4])
	filedata = filedata.replace('ATPOS06', xred[5])
	filedata = filedata.replace('ATPOS07', xred[6])
	filedata = filedata.replace('ATPOS08', xred[7])
	filedata = filedata.replace('ATPOS09', xred[8])
	filedata = filedata.replace('ATPOS10', xred[9])

	filedata = filedata.replace('ZXCV', str(celldm3))
    
with open('scf.in', 'w') as file:
	file.write(filedata)
        

