import os
import sys

def make_bash_niagara(filename, nodes=1, ntasks=40, time='04:00:00', mail_type = 'END,FAIL', mail_user = 'slurmnotifs@gmail.com', account ='rrg-maassenj', job_name = 'scf', executable = 'pw.x', qe_inputfile = 'scf.in', qe_outputfile = 'scf.out'):

    f = open(filename, 'w')
    f.write('#!/bin/bash\n')
    f.write('#SBATCH --nodes='+str(nodes)+'\n')
    f.write('#SBATCH --ntasks='+str(ntasks)+'\n')
    f.write('#SBATCH --time=' + time +'\n')
    f.write('#SBATCH --mail-type=' + mail_type+'\n')
    f.write('#SBATCH --mail-user=' + mail_user+'\n')
    f.write('#SBATCH --account=' + account+'\n')
    f.write('#SBATCH --job-name=' + job_name+'\n')
    f.write('\n')

    f.write('module load CCEnv \n')
    f.write('module load StdEnv \n')
    f.write('module load nixpkgs/16.09 \n')
    f.write('module load intel/2016.4 \n')
    f.write('module load openmpi/2.1.1 \n')
    f.write('module load quantumespresso/6.1 \n')
    f.write('\n')

    f.write('srun ' + executable + ' < ' + qe_inputfile + ' > ' + qe_outputfile +'\n')
    
    f.close()
    
    os.system('dos2unix ' + filename)
def make_bash_graham(filename, nodes=1, ntasks_per_node=32, time='04:00:00', mail_type = 'END,FAIL', mail_user = 'slurmnotifs@gmail.com', account ='def-maassenj', job_name = 'scf', executable = 'pw.x', qe_inputfile = 'scf.in', qe_outputfile = 'scf.out'):

    f = open(filename, 'w')
    f.write('#!/bin/bash\n')
    f.write('#SBATCH --nodes='+str(nodes)+'\n')
    f.write('#SBATCH --ntasks-per-node='+str(ntasks_per_node)+'\n')
    f.write('#SBATCH --time=' + time +'\n')
    f.write('#SBATCH --mail-type=' + mail_type+'\n')
    f.write('#SBATCH --mail-user=' + mail_user+'\n')
    f.write('#SBATCH --account=' + account+'\n')
    f.write('#SBATCH --job-name=' + job_name+'\n')
    f.write('\n')

    f.write('module load quantumespresso/6.1 \n')
    f.write('\n')

    f.write('srun ' + executable + ' < ' + qe_inputfile + ' > ' + qe_outputfile +'\n')
    
    f.close()
    
    os.system('dos2unix ' + filename)

if __name__ == "__main__":
    filename = sys.argv[1]
    make_bash_niagara(filename)
