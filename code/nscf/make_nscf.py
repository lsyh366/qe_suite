""" make_nscf(): Creates a Quantum Espresso input file for a non self-consistent calculation

"""
import os
import sys
import re


def make_nscf(filename, nbnd = 100, tolvrs=1e-8,  kpoints = '11x13x15auto', scf_inputfile = 'scf.in'):

    with open(scf_inputfile, 'r') as scf_inputfile:
        nscf_inputfile = open(filename, 'w')
        for num, line in enumerate(scf_inputfile, 0):
            if 'K_POINTS' in line:
                break
            if 'calculation' in line:
                nscf_inputfile.write("    calculation = 'nscf' \n")
            elif 'nbnd' in line:
                nscf_inputfile.write("    nbnd = " +str(nbnd) +" \n")
            elif 'tolvrs' in line:
                nscf_inputfile.write("    tolvrs = " +str(tolvrs) +" \n")
            else:
                nscf_inputfile.write(line)
        nscf_inputfile.close()
        scf_inputfile.close()
    
    

    os.system('cat ' + kpoints + '>>' + filename)
    os.system('dos2unix '+ filename)

if __name__ == "__main__":
    filename = sys.argv[1]
    make_nscf(filename)
