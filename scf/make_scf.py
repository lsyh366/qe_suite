""" make_scf_input(): Creates a Quantum Espresso input file for a self-consistent calculation

REQUIRED INPUTS
filename :       Name of SCF input file to be created
structure_file : Text file containing atomic structure info defining system on which the SCF calculation will be run
kpoint_list :    Text file defining k-point grid for SCF calculation
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

def make_scf_input(filename, structure_file, kpoint_list, prefix, scf_stencil = 'scf_stencil', restart_mode = 'from_scatch', wf_collect = '.false.', pseudo_dir = '../PP/', outdir = './', verbosity ='high', tprnfor = '.true.', tstress= '.true.', diagonalization = 'david', mixing_beta = 0.7, conv_thr = 1e-12, ecutwfc = 110, ecutrho = 1320, occupations = 'fixed', noncolin = '.true.', lspinorb = '.true.', london = '.true.', nbnd = 82):

    s = open(scf_stencil).read()
    s = s.replace('PREFIX', prefix)
    s = s.replace('RESTART_MODE', restart_mode)
    s = s.replace('WF_COLLECT', wf_collect)
    s = s.replace('PSEUDO_DIR', pseudo_dir)
    s = s.replace('OUTDIR', outdir)
    s = s.replace('VERBOSITY', verbosity)
    s = s.replace('TPRNFOR', tprnfor)
    s = s.replace('TSTRESS', tstress)

    s = s.replace('DIAGONALIZATION', diagonalization)
    s = s.replace('MIXING_BETA', str(mixing_beta))
    s = s.replace('CONV_THR', str(conv_thr))

    s = s.replace('ECUTWFC', str(ecutwfc))
    s = s.replace('ECUTRHO', str(ecutrho)) #Should be optional
    s = s.replace('OCCUPATIONS', occupations)
    s = s.replace('NONCOLIN', noncolin)
    s = s.replace('LSPINORB', lspinorb)
    s = s.replace('LONDON', london)
    s = s.replace('NBND', str(int(nbnd)))

    f = open(filename, 'w')
    f.write(s)
    f.close()

    os.system('cat ' + structure_file + ' >>' + filename)
    os.system('cat ' + kpoint_list + ' >>' + filename)
    os.system('dos2unix ' + filename)

if __name__ == "__main__":
    filename = sys.argv[1]
    structure_file = sys.argv[2]
    kpoint_list = sys.argv[3]
    prefix = sys.argv[4]
    make_scf(filename, structure_file, kpoint_list, prefix)
