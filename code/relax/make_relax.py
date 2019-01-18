""" make_relax_input(): Creates a Quantum Espresso input file for a self-consistent calculation

REQUIRED INPUTS
filename :       Name of pw.x input file to be created
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

def make_relax_input(filename, structure_file, kpoint_list, prefix='relax', relax_stencil = 'relax_stencil', calculation = 'vc-relax',nstep=500, restart_mode = 'from_scatch', wf_collect = 'false', pseudo_dir = '../PP/', outdir = './', verbosity ='high', tprnfor = 'true', tstress= 'true', etot_conv_thr = 1e-6, forc_conv_thr = 1e-5, diagonalization = 'david', mixing_beta = 0.7, conv_thr = 1e-12,electron_maxstep = 500, mixing_mode = 'plain', ion_dynamics = 'bfgs', pot_extrapolation='atomic', wfc_extrapolation = 'atomic', cell_dynamics = 'bfgs', wmass=0.002, cell_factor = 2.0, ecutwfc = 60, ecutrho = 120, occupations = 'fixed', noncolin = 'false', lspinorb = 'false', london = 'false', nbnd = 16):

    s = open(relax_stencil).read()
    s = s.replace('CALCULATION', calculation)
    s = s.replace('PREFIX', prefix)
    s = s.replace('RESTART_MODE', restart_mode)
    s = s.replace('WF_COLLECT', wf_collect)
    s = s.replace('PSEUDO_DIR', pseudo_dir)
    s = s.replace('OUTDIR', outdir)
    s = s.replace('VERBOSITY', verbosity)
    s = s.replace('TPRNFOR', tprnfor)
    s = s.replace('TSTRESS', tstress)
    s = s.replace('ETOT_CONV_THR', str(etot_conv_thr))
    s = s.replace('FORC_CONV_THR', str(forc_conv_thr))
    s = s.replace('NSTEP', str(int(nstep)))

    s = s.replace('DIAGONALIZATION', diagonalization)
    s = s.replace('MIXING_BETA', str(mixing_beta))
    s = s.replace('CONV_THR', str(conv_thr))
    s = s.replace('ELECTRON_MAXSTEP', str(electron_maxstep))
    s = s.replace('MIXING_MODE', str(mixing_mode))
    
    s = s.replace('ION_DYNAMICS', ion_dynamics)
    s = s.replace('POT_EXTRAPOLATION', pot_extrapolation)
    s = s.replace('WFC_EXTRAPOLATION', wfc_extrapolation)

    s = s.replace('CELL_DYNAMICS', cell_dynamics)
    s = s.replace('WMASS', str(wmass))
    s = s.replace('CELL_FACTOR', str(cell_factor))

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
    make_relax_input(filename, structure_file, kpoint_list)
