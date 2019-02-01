import numpy as np
import matplotlib.pyplot as plt


Ry2eV = 13.60569 #Conversion from Rydberg to eV
data = np.loadtxt('conv_plot_data')

ecuts  = np.array(data[:, 0]) 
energy = data[:, 1]
delta_energy = Ry2eV*np.array([abs(E - energy[-1]) for E in energy])
energy = np.array(energy)

plt.plot(Ry2eV*ecuts, np.log(delta_energy))
plt.axhline(y=-3, color='b') # 1 meV convergence
plt.xlabel('Energy cutoff (eV)')
plt.ylabel('Energy difference (log(eV))')
plt.title('Kinetic Energy Cutoff Convergence')
plt.show()

