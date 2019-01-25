""" make_scf_param(): Creates a Quantum Espresso input file for a self-consistent calculation

REQUIRED INPUTS
filename :       Name of SCF input file to be created
prefix :         Name given to charge density file output by SCF calculation

OPTIONAL INPUTS
pseudo_dir : Directory in which required pseudopotential files are located
outdir     : Directory into which output files from SCF calculation will be written
conv_thr   : Threshold dictating acceptable convergence in SCF cycle
ecutwfc    : Cutoff energy for wavefunctions
ecutrho    : Cutoff energy for charge density
nbnd       : Number of bands to include in SCF calculation

"""
import os
import sys

def make_scf_param(filename, prefix, restart_mode = 'from_scratch', wf_collect = '.false.', pseudo_dir = '../PP/', outdir = './', verbosity ='high', tprnfor = '.true.', tstress= '.true.', diagonalization = 'david', mixing_beta = 0.7, conv_thr = 1e-12, ecutwfc = 110, ecutrho = 1320, occupations = 'fixed', noncolin = '.true.', lspinorb = '.true.', london = '.true.', nbnd = 82, nat = 5, ntyp = 2):

    f = open(filename, 'w+')
    f.write(' &control\n')
    f.write("   calculation     = 'scf'\n" )
    f.write("   prefix          = '" + prefix + "'\n" )
    f.write("   restart_mode    = '" + restart_mode + "'\n" )
    f.write('   wf_collect      = ' + wf_collect + "\n" )
    f.write("   pseudo_dir      = '" + pseudo_dir + "'\n" )
    f.write("   outdir          = '" + outdir + "'\n" )
    f.write("   verbosity       = '" + verbosity + "'\n" )
    f.write('   tprnfor         = ' + tprnfor + "\n" )
    f.write('   tstress         = ' + tstress + "\n" )
    f.write(' /\n')

    f.write(' &system\n')
    f.write('   ecutwfc     =' +str(ecutwfc) +'\n')
    f.write('   ecutrho     =' +str(ecutrho) +'\n')
    f.write('   nbnd        =' +str(nbnd) +'\n')
    f.write('   nat         =' +str(nat) +'\n')
    f.write('   ntyp        =' +str(ntyp) +'\n')
    f.write('   noncolin    = ' + noncolin + "\n" )
    f.write('   lspinorb    = ' + lspinorb + "\n" )
    f.write('   london      = ' + london + "\n" )
    f.write(' /\n')
    
    f.write(' &electrons\n')
    f.write("   diagonalization = '" + diagonalization + "'\n")
    f.write('   mixing_beta     =' +str(mixing_beta) +'\n')
    f.write('   conv_thr        =' +str(conv_thr) +'\n')

    f.close()


    #os.system('cat ' + structure_file + ' >>' + filename)
    #os.system('cat ' + kpoint_list + ' >>' + filename)
    #os.system('dos2unix ' + filename)

if __name__ == "__main__":
    filename = sys.argv[1]
    prefix = sys.argv[2]
    make_scf_param(filename, prefix)
