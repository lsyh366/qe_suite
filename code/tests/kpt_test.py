import sys
import os
sys.path.insert(0, "/scratch/m/maassenj/cmrudder/bin")

from QL_struct_makers import make_Bi2Te3_QL
from kpts_makers import make_auto_kpts
from param_makers import make_scf_param
from bash_makers import make_bash_niagara 

values = [5,7,9,11]
make_Bi2Te3_QL('STRUCT')
make_scf_param('PARAMS', prefix='Bi2Te3_QL', pseudo_dir = '../../PP/')
N = len(values)

for k in range(N):
    iteration = 'k' + str(values[k])
    os.system('mkdir ' + iteration)
    make_auto_kpts('KPTS', grid = [values[k], values[k], 1, 0, 0 ,0])
    os.system('cat PARAMS STRUCT KPTS >> scf.in')
    os.system('dos2unix scf.in')
    os.system('mv scf.in  ' + iteration)

    make_bash_niagara('scf.sh', job_name = 'Bi2Te3_QL' +'_' + iteration)
    os.system('mv scf.sh ' + iteration)

    os.chdir(iteration)
    os.system('sbatch scf.sh')
    os.chdir('..')

os.system('rm -f PARAMS STRUCT KPTS')


