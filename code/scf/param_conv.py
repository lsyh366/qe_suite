import os
import numpy as np
from make_scf import make_scf_input
from bash_makers import make_bash_niagara
from scf_scrape import get_scf_dict
""" param_conv_test(): Creates the directories and files necessary for a convergence test (of QE SCF calculations) to be performed on Compute Canada's Niagara cluster. 

REQUIRED INPUTS
 material  :       Name given to material being studied, e.g 'Bi2Te3_2QL'
 parameter :       Name of keyword argument to be varied, i.e ecutwfc, ecutrho, etc.
 values    :       List or 1D array of values, eg. [60, 70, 80, 90, 100]
 """
 
def param_conv_test(material, parameter, values):
    N = len(values) #number of tests
    struct_file = 'Bi2Te3_QL_exp'
    kpoint_file = '11x11x11auto'

    for k in range(N):
        name = parameter + str(values[k])
        os.system('mkdir ' + name)
        
        make_scf_input('scf.in', struct_file, kpoint_file, name, **{parameter : values[k]}) 
        os.system("mv scf.in " + name)

        make_bash_niagara('scf.sh', job_name = material + '_' + name)
        os.system("mv scf.sh " + name)

        os.chdir(name)
        print(name)
        #os.system('sbatch scf.sh')
        os.chdir('..')

param_conv_test('Bi2Te3_QL', 'ecutwfc', [100, 120, 140])

def param_conv_scrape(parameter, values):
    dict_list = []
    for k in range(N):
        name = parameter + str(values[k])
        os.chdir(name)
        scf_dict = get_scf_dict('scf.out', name) #pickles single dictionary
        dict_list.append(scf_dict)
        os.chdir('..')
    
    return dict_list

