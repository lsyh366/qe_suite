import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('conv_plot_data')

ecuts  = np.array(data[:, 0]) 
energy = data[:, 1]
delta_energy = np.array([abs(E - energy[-1]) for E in energy])
energy = np.array(energy)

plt.plot(ecuts, np.log(delta_energy))
plt.xlabel('Energy cutoff (Ry)')
plt.ylabel('Energy difference (log scale)')
plt.title('Kinetic Energy Cutoff Convergence')
plt.show()

