
# coding: utf-8

# In[24]:


import numpy as np
import re
import os 
import sys
import nltk
import pickle
#nltk.download('punkt')


# In[25]:


def file_len(fname):
    with open(fname) as f:
        for i in enumerate(f,1):
            pass
    return i[0]


# In[26]:


def last_line(string, file):
    counter = 0
    with open(file) as file:
        for num, line in enumerate(file, 0):
            if string in line:
                counter = num
    return counter


# In[27]:


def first_line(string, file):
    with open(file) as file:
        for num, line in enumerate(file, 0):
            if string in line:
                break
    return num


# In[32]:


def get_natoms(relax_output_file):
     
    file = open(relax_output_file)
    for line in file:
        x = re.findall('number of atoms', line)
        if len(x)>0:
            natoms = re.sub("[^0-9]", "", line)
            natoms = int(natoms)
    return natoms


# In[163]:


def get_relax_dict(relax_output_file, pickle_name, struct_file_name):
    
    file = open(relax_output_file)
    struct_file = open(struct_file_name, 'w+')
    lines = file.readlines()
    relax_dict = {}
    
    natoms = get_natoms(relax_output_file)
    relax_dict['natoms'] = natoms
            
    num_lines = file_len(relax_output_file)
    #Relaxed Structure
    for k in range(num_lines):
        line = lines[k]
        if 'Begin final coordinates' in line:
            for i in range(k+3, k+9+natoms):
                struct_file.write(lines[i])
    struct_file.write('\n')
    struct_file.close()
    file.close()
    
    stress_line = last_line('total   stress', relax_output_file)
    
    #Row vectors making up the total stress tensor(Ry/bohr**3)
    total1 = nltk.word_tokenize(lines[stress_line +1])[0:3]
    total1 = np.array([float(k) for k in total1])
    total2 = nltk.word_tokenize(lines[stress_line +2])[0:3]
    total2 = np.array([float(k) for k in total2])
    total3 = nltk.word_tokenize(lines[stress_line +3])[0:3]
    total3 = np.array([float(k) for k in total3])
    
    total_stress = np.array([total1, total2, total3])
    relax_dict['total_stress'] = total_stress
    
    #Kinetic stress tensor
    kin1 = nltk.word_tokenize(lines[stress_line +5])[-3:]
    kin1 = np.array([float(k) for k in kin1])
    kin2 = nltk.word_tokenize(lines[stress_line +6])[-3:]
    kin2 = np.array([float(k) for k in kin2])
    kin3 = nltk.word_tokenize(lines[stress_line +7])[-3:]
    kin3 = np.array([float(k) for k in kin3])
    
    kinetic_stress = np.array([kin1, kin2, kin3])
    relax_dict['kinetic_stress'] = kinetic_stress
    
    #Local stress tensor
    local1 = nltk.word_tokenize(lines[stress_line +9])[-3:]
    local1 = np.array([float(k) for k in local1])
    local2 = nltk.word_tokenize(lines[stress_line +10])[-3:]
    local2 = np.array([float(k) for k in local2])
    local3 = nltk.word_tokenize(lines[stress_line +11])[-3:]
    local3 = np.array([float(k) for k in local3])
    
    local_stress = np.array([local1, local2, local3])
    relax_dict['local_stress'] = local_stress
    
    #Local stress tensor
    nonlocal1 = nltk.word_tokenize(lines[stress_line +13])[-3:]
    nonlocal1 = np.array([float(k) for k in nonlocal1])
    nonlocal2 = nltk.word_tokenize(lines[stress_line +14])[-3:]
    nonlocal2 = np.array([float(k) for k in nonlocal2])
    nonlocal3 = nltk.word_tokenize(lines[stress_line +15])[-3:]
    nonlocal3 = np.array([float(k) for k in nonlocal3])
    
    nonlocal_stress = np.array([nonlocal1, nonlocal2, nonlocal3])
    relax_dict['nonlocal_stress'] = nonlocal_stress
    
    #Hartree stress tensor
    hart1 = nltk.word_tokenize(lines[stress_line +17])[-3:]
    hart1 = np.array([float(k) for k in hart1])
    hart2 = nltk.word_tokenize(lines[stress_line +18])[-3:]
    hart2 = np.array([float(k) for k in hart2])
    hart3 = nltk.word_tokenize(lines[stress_line +19])[-3:]
    hart3 = np.array([float(k) for k in hart3])
    
    hartree_stress = np.array([hart1, hart2, hart3])
    relax_dict['hartree_stress'] = hartree_stress
    
    #Exchange correlation stress tensor
    excor1 = nltk.word_tokenize(lines[stress_line +21])[-3:]
    excor1 = np.array([float(k) for k in excor1])
    excor2 = nltk.word_tokenize(lines[stress_line +22])[-3:]
    excor2 = np.array([float(k) for k in excor2])
    excor3 = nltk.word_tokenize(lines[stress_line +23])[-3:]
    excor3 = np.array([float(k) for k in excor3])
    
    excor_stress = np.array([excor1, excor2, excor3])
    relax_dict['excor_stress'] = excor_stress
    
    #Core correction stress tensor
    corecor1 = nltk.word_tokenize(lines[stress_line +25])[-3:]
    corecor1 = np.array([float(k) for k in corecor1])
    corecor2 = nltk.word_tokenize(lines[stress_line +26])[-3:]
    corecor2 = np.array([float(k) for k in corecor2])
    corecor3 = nltk.word_tokenize(lines[stress_line +27])[-3:]
    corecor3 = np.array([float(k) for k in corecor3])
    
    corecor_stress = np.array([corecor1, corecor2, corecor3])
    relax_dict['corecor_stress'] = corecor_stress
    
    #Ewald stress tensor
    ewald1 = nltk.word_tokenize(lines[stress_line +29])[-3:]
    ewald1 = np.array([float(k) for k in ewald1])
    ewald2 = nltk.word_tokenize(lines[stress_line +30])[-3:]
    ewald2 = np.array([float(k) for k in ewald2])
    ewald3 = nltk.word_tokenize(lines[stress_line +31])[-3:]
    ewald3 = np.array([float(k) for k in ewald3])
    
    ewald_stress = np.array([ewald1, ewald2, ewald3])
    relax_dict['ewald_stress'] = ewald_stress
    
    #Hubbard stress tensor
    hub1 = nltk.word_tokenize(lines[stress_line +33])[-3:]
    hub1 = np.array([float(k) for k in hub1])
    hub2 = nltk.word_tokenize(lines[stress_line +34])[-3:]
    hub2 = np.array([float(k) for k in hub2])
    hub3 = nltk.word_tokenize(lines[stress_line +35])[-3:]
    hub3 = np.array([float(k) for k in hub3])
    
    hubbard_stress = np.array([hub1, hub2, hub3])
    relax_dict['hubbard_stress'] = hubbard_stress
    
    #London stress tensor
    lon1 = nltk.word_tokenize(lines[stress_line +37])[-3:]
    lon1 = np.array([float(k) for k in lon1])
    lon2 = nltk.word_tokenize(lines[stress_line +38])[-3:]
    lon2 = np.array([float(k) for k in lon2])
    lon3 = nltk.word_tokenize(lines[stress_line +39])[-3:]
    lon3 = np.array([float(k) for k in lon3])
    
    london_stress = np.array([lon1, lon2, lon3])
    relax_dict['london_stress'] = london_stress
    
    #XDM stress tensor
    xdm1 = nltk.word_tokenize(lines[stress_line +41])[-3:]
    xdm1 = np.array([float(k) for k in xdm1])
    xdm2 = nltk.word_tokenize(lines[stress_line +42])[-3:]
    xdm2 = np.array([float(k) for k in xdm2])
    xdm3 = nltk.word_tokenize(lines[stress_line +43])[-3:]
    xdm3 = np.array([float(k) for k in xdm3])
    
    xdm_stress = np.array([xdm1, xdm2, xdm3])
    relax_dict['xdm_stress'] = xdm_stress
    
    #DFT-NL stress tensor
    dft1 = nltk.word_tokenize(lines[stress_line +45])[-3:]
    dft1 = np.array([float(k) for k in dft1])
    dft2 = nltk.word_tokenize(lines[stress_line +46])[-3:]
    dft2 = np.array([float(k) for k in dft2])
    dft3 = nltk.word_tokenize(lines[stress_line +47])[-3:]
    dft3 = np.array([float(k) for k in dft3])
    
    dftnl_stress = np.array([dft1, dft2, dft3])
    relax_dict['dftnl_stress'] = dftnl_stress
    
    #TS-vdW stress tensor
    vdw1 = nltk.word_tokenize(lines[stress_line +45])[-3:]
    vdw1 = np.array([float(k) for k in vdw1])
    vdw2 = nltk.word_tokenize(lines[stress_line +46])[-3:]
    vdw2 = np.array([float(k) for k in vdw2])
    vdw3 = nltk.word_tokenize(lines[stress_line +47])[-3:]
    vdw3 = np.array([float(k) for k in vdw3])
    
    tsvdw_stress = np.array([vdw1, vdw2, vdw3])
    relax_dict['tsvdw_stress'] = tsvdw_stress
    
    force_line = last_line('Forces acting on atoms', relax_output_file)
    forces = []
    nonlocal_forces = []
    ionic_forces = []
    local_forces = []
    corecor_forces = []
    hubbard_forces = []
    scf_forces = []
    
    def get_force_data(line):
        data_list = []
        line = nltk.word_tokenize(line)
        #data_list.append(line[1]) #Atom number
        data_list.append(line[3]) #Atomic type
        data_list.append(line[-3]) #Force components
        data_list.append(line[-2])
        data_list.append(line[-1])
    
        return data_list
    
    for k in range(natoms):
        forces.append(get_force_data(lines[force_line + 2 +k]))
        nonlocal_forces.append(get_force_data(lines[force_line + 3+natoms+k]))
        ionic_forces.append(get_force_data(lines[force_line + 4+2*natoms+k]))
        local_forces.append(get_force_data(lines[force_line + 5+3*natoms+k]))
        corecor_forces.append(get_force_data(lines[force_line + 6+4*natoms+k]))
        hubbard_forces.append(get_force_data(lines[force_line + 7+5*natoms+k]))
        scf_forces.append(get_force_data(lines[force_line + 8+6*natoms+k]))
        
        
    forces = np.array(forces)
    relax_dict['forces'] = forces
    
    nonlocal_forces = np.array(nonlocal_forces)
    relax_dict['nonlocal_forces'] = nonlocal_forces
    
    ionic_forces = np.array(ionic_forces)
    relax_dict['ionic_forces'] = ionic_forces
    
    local_forces = np.array(local_forces)
    relax_dict['local_forces'] = local_forces
    
    corecor_forces = np.array(corecor_forces)
    relax_dict['corecor_forces'] = corecor_forces
    
    hubbard_forces = np.array(hubbard_forces)
    relax_dict['hubbard_forces'] = hubbard_forces
    
    scf_forces = np.array(scf_forces)
    relax_dict['scf_forces'] = scf_forces
    
    return relax_dict


# In[166]:


relax_dict = get_relax_dict('relax.out', 'picklepickle', 'relaxed_struct')
relax_dict['scf_forces']

