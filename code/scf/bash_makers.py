""" make_bash(): Creates a Quantum Espresso input file for a self-consistent calculation

"""
import os
import sys

def make_bash_niagara(filename, bash_stencil = 'bash_stencil', nodes=1, ntasks=40, time='04:00:00', mail_type = 'END,FAIL', mail_user = 'slurmnotifs@gmail.com', account ='rrg-maassenj', job_name = 'scf', executable = 'pw.x', qe_inputfile = 'scf.in', qe_outputfile = 'scf.out'):

    s = open(bash_stencil).read()
    s = s.replace('NODES', str(nodes))
    s = s.replace('NTASKS', str(ntasks))
    s = s.replace('TIME', time)
    s = s.replace('MAIL-TYPE', mail_type)
    s = s.replace('MAIL-USER', mail_user)
    s = s.replace('ACCOUNT', account)
    s = s.replace('JOB-NAME', job_name)

    s = s.replace('EXECUTABLE', executable)
    s = s.replace('QE_INPUTFILE', qe_inputfile)
    s = s.replace('QE_OUTPUTFILE', qe_outputfile)


    f = open(filename, 'w')
    f.write(s)
    f.close()
    
    os.system('dos2unix ' + filename)
if __name__ == "__main__":
    filename = sys.argv[1]
    make_bash_niagara(filename)
