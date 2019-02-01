import sys
import os
import numpy as np
sys.path.insert(0, "/scratch/m/maassenj/cmrudder/bin")

from scf_scrape import get_scf_dict

values = [5*k +40 for k in range(12)] #Taken from testing script

total_energies = []
data_dir = 'test_data'     #Name of directory to store output files
os.system('mkdir ' + data_dir)
N = len(values)

for k in range(N):
    iteration = 'ecutwfc' + str(values[k])
    os.chdir(iteration)
    
    os.system('cp scf.out ../' + data_dir + '/' + iteration +'.out') 
    scf_dict = get_scf_dict('scf.out', iteration + '_pickle') 
    total_energies.append(scf_dict['total_energy'])
    
    os.chdir('..')
    os.system('rm -rf ' + iteration)


conv_plot_data = np.column_stack((values, total_energies))
np.savetxt('conv_plot_data', conv_plot_data)
os.system('mv conv_plot_data ' + data_dir + '/')
print('ecutwfc values = ', values)
print('Total energies = ', total_energies)
