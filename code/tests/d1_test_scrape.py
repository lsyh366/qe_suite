import sys
import os
sys.path.insert(0, "/scratch/m/maassenj/cmrudder/bin")

from scf_scrape import get_scf_dict

values = [0.9, 1, 1.1]# Interatomic spacing values used
total_energies = []

N = len(values)

for k in range(N):
    iteration = 'd1_' + str(values[k])
    os.chdir(iteration)
    scf_dict = get_scf_dict('scf.out', iteration + '_pickle') #Saves data to pickle
    total_energies.append(scf_dict['total_energy'])
    os.chdir('..')

print('Spacings = ', values)
print('Total energies = ', total_energies)
