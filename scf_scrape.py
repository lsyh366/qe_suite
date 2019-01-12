import numpy as np 
import re
import os
import sys
import nltk
#nltk.download('punkt')

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
        
    
    
        return vectors, rec_vectors, atom_types, cart_atoms, cryst_atoms,

def scf_summary(output_file):
    file = open(output_file)
    
    for line in file:
        
        x = re.findall('!', line)
        if len(x) >0:
            total_energy = re.sub("[^0-9-.]", "", line)
            total_energy = float(total_energy)
        x = re.findall('lattice parameter', line)
        if len(x)>0:
            alat= re.sub("[^0-9-.]", "", line) #Will have two extra dots at end of number
            alat = float(alat[:-2])   
        x = re.findall('number of atoms/cell', line)
        if len(x) > 0:
            natoms = re.sub("[^0-9]", "", line)
            natoms = int(natoms)
        x = re.findall('number of atomic types', line)
        if len(x) >0:
            ntypes = re.sub("[^0-9]", "", line)
            ntypes = int(ntypes)
        x = re.findall('kinetic-energy cutoff', line)
        if len(x) >0:
            ecutwfc = re.sub("[^0-9-.]", "", line) #Will have extra hyphen at beginning
            ecutwfc = float(ecutwfc[1:])
        x = re.findall('charge density cutoff', line)
        if len(x) >0:
            ecutrho = re.sub("[^0-9-.]", "", line)
            ecutrho = float(ecutrho)
        x = re.findall('convergence threshold', line)
        if len(x) > 0:
            conv_thr = re.sub("[^0-9-.-E]", "", line) #Will have extra = at beginning
            conv_thr = float(conv_thr[1:])
        x = re.findall('mixing beta', line)
        if len(x) >0:
            mixing_beta = re.sub("[^0-9-.]", "", line)
            mixing_beta = float(mixing_beta)
        x = re.findall('number of electrons', line)
        if len(x) > 0:
            num_electrons = re.sub("[^0-9-.]", "", line)
            num_electrons = int(float(num_electrons))
        x = re.findall('number of Kohn-Sham states', line)
        if len(x) >0:
            nbnd = re.sub("[^0-9]", "", line)
            nbnd = int(float(nbnd))

    vectors, rec_vectors, atom_types, cart_atoms, cryst_atoms = get_structure(output_file)
    a1, a2, a3 = vectors[0], vectors [1], vectors[2]
    b1, b2, b3 = rec_vectors[0], rec_vectors[1], rec_vectors[2]
    
    print('Cartesian Lattice Vectors (a.u.)')
    print('a1 = ', a1)
    print('a2 = ', a2)
    print('a3 = ', a3)
    print('')
    #print('Cartesian Reciprocal Lattice Vectors (a.u.)^-1')
    #print('b1 =', b1)
    #print('b2 =', b2)
    #print('b3 =', b3)
    #print('')
    print('Atomic Species')
    print(atom_types)
    print('')
    print('Cartesian Atomic positions (a.u.)')
    print(cart_atoms)
    print('')
    #print('Crystallographic atomic positions')
    #print(cryst_atoms)
    #print('')
    #print('Lattice parameter = ' + str(alat) + ' (a.u.)')
    #print('Number of atoms = ' + str(natoms))
    #print('Number of atomic species = ' + str(ntypes))  
    print('Wavefunction energy cutoff = ' + str(ecutwfc) + ' Rydberg')
    print('Charge density cutoff = ' + str(ecutrho) + ' Rydberg')
    print('Convergence threshold = ' + str(conv_thr))
    #print('Mixing beta = ' , mixing_beta)
    print('Number of electrons = ', num_electrons)
    print('Number of Kohn-Sham states = ', nbnd)
    print('')
    print('Total energy = ' + str(total_energy) + ' Rydberg')    


if __name__ == "__main__" :
    print('')
    file_to_summarize = sys.argv[1]
    scf_summary(file_to_summarize)

