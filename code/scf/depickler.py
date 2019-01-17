import pickle
import numpy as np
import matplotlib.pyplot as plt
import sys

pickle_name =sys.argv[1]

scf_dict = pickle.load( open(pickle_name, 'rb'))

print('Total_energy = ', scf_dict['total_energy'])
