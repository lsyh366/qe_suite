import pickle
import numpy as np
import matplotlib.pyplot as plt
import sys

pickle_name =sys.argv[1]

scf_dict = pickle.load( open(pickle_name, 'rb'))

accuracies = scf_dict['accuracies']
hf_estimates = scf_dict['hf_estimates']
total_energies = scf_dict['total_energies']
total_cpu_time = scf_dict['total_cpu_time']


true_energy = total_energies[-1]



plt.figure()
plt.plot(total_cpu_time, 'ko')
plt.ylabel('Elapsed time (s)')
plt.xlabel('Iteration Number')
plt.title('SCF Convergence Cycle') 
plt.show()

plt.figure()
plt.plot(np.log10(accuracies), 'ko')
plt.ylabel('log10(Accuracy)')
plt.xlabel('Iteration Number')
plt.title('SCF Convergence Cycle') 
plt.show()
