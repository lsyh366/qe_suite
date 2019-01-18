import numpy as np 
import re
import os
import sys
import nltk
import pickle
#nltk.download('punkt')

def file_len(fname):
    with open(fname) as f:
        for i in enumerate(f,1):
            pass
    return i[0] 

def last_line(string, file):
            """Returns line number of last occurence of a given string in a given file"""
            counter = 0
            with open(file) as file:
                for num, line in enumerate(file,0):
                    if string in line:
                        counter = num
                   
            return counter
        
def first_line(string, file):
            "Returns line number of first occurence of a given string in a given file"
            with open(file) as file:
                for num, line in enumerate(file, 0):
                    if string in line:
                        break
            return num

def get_structure(output_file):
        """Returns the basis vectors of the direct and reciprocal lattices in atomic units,
        as well as the atomic positions in both Cartesian and crystallographic coordinates"""
        file = open(output_file)
        #lines = file.readlines()
        
        for line in file:
            x = re.findall('lattice parameter', line)
            if len(x)>0:
                alat= re.sub("[^0-9-.]", "", line) #Will have two extra dots at end of number because of (a.u.)
                alat = float(alat[:-2])
                
            x = re.findall('number of atoms/cell', line)
            if len(x) >0:
                natoms = re.sub("[^0-9]", "", line)
                natoms = int(float(natoms))
                
    
        crystal_line = last_line('crystal axes', output_file)
        reciprocal_line = last_line('reciprocal axes', output_file)
        cart_atoms_line = first_line('site n.', output_file)  
        cryst_atoms_line = last_line('site n.', output_file)
        
        file = open(output_file)
        lines = file.readlines()
        a1 = nltk.word_tokenize(lines[crystal_line +1])[-4:-1]
        a2 = nltk.word_tokenize(lines[crystal_line + 2])[-4:-1]
        a3 = nltk.word_tokenize(lines[crystal_line +3])[-4:-1]
        a1 = alat*np.array([float(k) for k in a1])
        a2 = alat*np.array([float(k) for k in a2])
        a3 = alat*np.array([float(k) for k in a3])
        vectors = [a1, a2, a3]
        
        b1 = nltk.word_tokenize(lines[reciprocal_line +1])[-4:-1]
        b2 = nltk.word_tokenize(lines[reciprocal_line +2])[-4:-1]
        b3 = nltk.word_tokenize(lines[reciprocal_line +3])[-4:-1]
        b1 = 2*np.pi*np.array([float(k) for k in b1])/alat
        b2 = 2*np.pi*np.array([float(k) for k in b2])/alat
        b3 = 2*np.pi*np.array([float(k) for k in b3])/alat
        rec_vectors = [b1, b2, b3]
        
        cart_atoms = np.zeros([natoms, 3])
        cryst_atoms = np.zeros([natoms, 3])
        atom_types = []
        for k in range(natoms):
            atom_types.append(nltk.word_tokenize(lines[cart_atoms_line +k+1])[1])
            atom_pos = nltk.word_tokenize(lines[cart_atoms_line +k+1])[-4:-1]
            cart_atoms[k, :] = alat*np.array([float(i) for i in atom_pos])
            atom_pos = nltk.word_tokenize(lines[cryst_atoms_line +k+1])[-4:-1]
            cryst_atoms[k, :] = np.array([float(i) for i in atom_pos])
        
    
    
        return np.array(vectors), np.array(rec_vectors), atom_types, np.array(cart_atoms), np.array(cryst_atoms)

def get_scf_convergence(output_file):
    
    accuracies = []
    hf_estimates=[]
    total_energies = []
    total_cpu_time = []

    num_lines = file_len(output_file)
    file = open(output_file)
    lines = file.readlines()

    for k in range(num_lines):
        line = lines[k]
        if 'estimated scf accuracy' in line:
            accuracies.append(float(nltk.word_tokenize(line)[-2]))
            upone = lines[k-1]
            uptwo = lines[k-2]
            hf_estimates.append(float(nltk.word_tokenize(upone)[-2]))
            total_energies.append(float(nltk.word_tokenize(uptwo)[-2]))
        if 'total cpu time spent up to now' in line:
            total_cpu_time.append(float(nltk.word_tokenize(line)[-2]))
    return np.array(accuracies), np.array(hf_estimates), np.array(total_energies), np.array(total_cpu_time)

def get_scf_dict(scf_output_file, pickle_name):

    file = open(scf_output_file)
    scf_dict = {}
    for line in file:
        
        x = re.findall('!', line)
        if len(x) >0:
            total_energy = re.sub("[^0-9-.]", "", line)
            total_energy = float(total_energy)
            scf_dict['total_energy'] = total_energy
        x = re.findall('lattice parameter', line)
        if len(x)>0:
            alat= re.sub("[^0-9-.]", "", line) #Will have two extra dots at end of number
            alat = float(alat[:-2]) 
            scf_dict['alat'] = alat
        x = re.findall('number of atoms/cell', line)
        if len(x) > 0:
            natoms = re.sub("[^0-9]", "", line)
            natoms = int(natoms)
            scf_dict['natoms'] = natoms
        x = re.findall('number of atomic types', line)
        if len(x) >0:
            ntypes = re.sub("[^0-9]", "", line)
            ntypes = int(ntypes)
            scf_dict['ntypes'] = ntypes
        x = re.findall('kinetic-energy cutoff', line)
        if len(x) >0:
            ecutwfc = re.sub("[^0-9-.]", "", line) #Will have extra hyphen at beginning
            ecutwfc = float(ecutwfc[1:])
            scf_dict['ecutwfc'] = ecutwfc
        x = re.findall('charge density cutoff', line)
        if len(x) >0:
            ecutrho = re.sub("[^0-9-.]", "", line)
            ecutrho = float(ecutrho)
            scf_dict['ecutrho'] = ecutrho
        x = re.findall('convergence threshold', line)
        if len(x) > 0:
            conv_thr = re.sub("[^0-9-.-E]", "", line) #Will have extra = at beginning
            conv_thr = float(conv_thr[1:])
            scf_dict['conv_thr'] = conv_thr
        x = re.findall('mixing beta', line)
        if len(x) >0:
            mixing_beta = re.sub("[^0-9-.]", "", line)
            mixing_beta = float(mixing_beta)
            scf_dict['mixing_beta'] = mixing_beta
        x = re.findall('number of electrons', line)
        if len(x) > 0:
            num_electrons = re.sub("[^0-9-.]", "", line)
            num_electrons = int(float(num_electrons))
            scf_dict['num_electrons'] = num_electrons
        x = re.findall('number of Kohn-Sham states', line)
        if len(x) >0:
            nbnd = re.sub("[^0-9]", "", line)
            nbnd = int(float(nbnd))
            scf_dict['nbnd'] = nbnd
    vectors, rec_vectors, atom_types, cart_atoms, cryst_atoms = get_structure(scf_output_file)
    accuracies, hf_estimates, total_energies, total_cpu_time = get_scf_convergence(scf_output_file)

    scf_dict['vectors'] = vectors
    scf_dict['rec_vectors'] = rec_vectors
    scf_dict['cart_atoms'] = cart_atoms
    scf_dict['cryst_atoms'] = cryst_atoms
    scf_dict['atom_types'] = atom_types
    
    scf_dict['accuracies'] = accuracies
    scf_dict['hf_estimates'] = hf_estimates
    scf_dict['total_energies'] = total_energies
    scf_dict['total_cpu_time'] = total_cpu_time

    pickle.dump(scf_dict, open(pickle_name, 'wb'))
    
    return scf_dict

def scf_summary(scf_dict):

    vectors = scf_dict['vectors']
    rec_vectors = scf_dict['rec_vectors']
    cart_atoms = scf_dict['cart_atoms']
    cryst_atoms = scf_dict['cryst_atoms']
    atom_types = scf_dict['atom_types']

    a1, a2, a3 = vectors[0], vectors [1], vectors[2]
    b1, b2, b3 = rec_vectors[0], rec_vectors[1], rec_vectors[2]
    
    print('Cartesian Lattice Vectors (a.u.)')
    print('a1 = ', a1)
    print('a2 = ', a2)
    print('a3 = ', a3)
   
    print('')
    print('Cartesian Reciprocal Lattice Vectors (2*pi/a.u.)')
    print('b1 = ', b1)
    print('b2 = ', b2)
    print('b3 = ', b3)


    print('')
    print('Atomic Species')
    print(atom_types)
    
    print('')
    print('Cartesian Atomic positions (a.u.)')
    print(cart_atoms)
    
    print('')
    print('Wavefunction energy cutoff = ' + str(scf_dict['ecutwfc']) + ' Rydberg')
    print('Charge density cutoff = ' + str(scf_dict['ecutrho']) + ' Rydberg')
    print('Convergence threshold = ' + str(scf_dict['conv_thr']))
    print('Number of electrons = ', scf_dict['num_electrons'])
    print('Number of Kohn-Sham states = ', scf_dict['nbnd'])
    print('')
    print('Total energy = ' + str(scf_dict['total_energy']) + ' Rydberg')    


if __name__ == "__main__" :
    print('')
    output_file = sys.argv[1]
    pickle_name = sys.argv[2]
    scf_summary(get_scf_dict(output_file, pickle_name))

