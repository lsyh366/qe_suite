import sys
import os
sys.path.insert(0, "/scratch/m/maassenj/cmrudder/bin")

from scf_scrape import get_scf_dict

values = [50,55,60]# Values of ecutwfc used (must match test)
total_energies = [] # Quantity to be scraped (in this case total energy)
N = len(values)

for k in range(N):
    iteration = 'ecutwfc' + str(values[k])
    os.chdir(iteration)
    scf_dict = get_scf_dict('scf.out', iteration + '_pickle') #Saves data to pickle
    total_energies.append(scf_dict['total_energy'])
    os.chdir('..')

print('ecutwfc = ', values)
print('Total energy = ', total_energies)
