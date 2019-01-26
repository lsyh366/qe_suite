import sys
import os
sys.path.insert(0, "/scratch/m/maassenj/cmrudder/bin")

from QL_struct_makers import make_Bi2Te3_QL
from kpts_makers import make_auto_kpts
from param_makers import make_scf_param
from bash_makers import make_bash_niagara 

values = [0.9, 1, 1.1]
make_scf_param('PARAMS', prefix='Bi2Te3_QL', pseudo_dir = '../../PP/')
make_auto_kpts('KPTS', grid = [11,11, 1, 0, 0 ,0])
N = len(values)

for k in range(N):
    iteration = 'd1_' + str(values[k])
    os.system('mkdir ' + iteration)
    make_Bi2Te3_QL('STRUCT', D1 = values[k])
    os.system('cat PARAMS STRUCT KPTS >> scf.in')
    os.system('dos2unix scf.in')
    os.system('mv scf.in  ' + iteration)

    make_bash_niagara('scf.sh', job_name = 'Bi2Te3_QL' +'_' + iteration)
    os.system('mv scf.sh ' + iteration)

    os.chdir(iteration)
    os.system('sbatch scf.sh')
    os.chdir('..')

os.system('rm -f PARAMS STRUCT KPTS')


