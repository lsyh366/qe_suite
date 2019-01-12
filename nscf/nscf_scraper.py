import numpy as np 
import pandas as pd
import os
import re
import sys
import pickle
import nltk
#nltk.download('punkt')

def nscf_scraper(input_file):

   
    file = open(input_file)
    lines = file.readlines()
    
    def last_line(string): #Returns line number of last occurence of a given string
        with open(input_file) as file:
            for num, line in enumerate(file,0):
                if string in line:
                    last_line = num
        return last_line

    n_bands = abs(int(re.sub("[^0-9-.]", "",lines[last_line('Kohn-Sham')])))
    
    kpt_line = last_line('number of k points=')
    n_kpts = abs(int(re.sub("[^0-9-.]", "",lines[last_line('number of k points=')])))
    
    bandstructure = np.zeros((n_kpts, n_bands+4))
    
    for k in range(n_kpts):
        temp = nltk.word_tokenize(lines[kpt_line +2 +k])
        temp = temp[6:] 
        del temp[3:7]
        for j in range(4):
            temp[j] = float(temp[j])
        temp = np.array(temp)
        bandstructure[k, 0:4] = temp

    end_line = last_line('End of band structure calculation')

    band_rows = int(np.ceil(n_bands/8))

    for j in range(n_kpts):
        for k in range(band_rows-1):
            temp = nltk.word_tokenize(lines[end_line+4+k+j*(2*band_rows+5)])
            for l in range(len(temp)):
                temp[l] = float(temp[l])
            temp = np.array(temp)
            bandstructure[j,k*8+4:k*8+12] = temp
        temp = nltk.word_tokenize(lines[end_line+4+j*(2*band_rows+5)+band_rows-1]) #Last row (possibly shorter)
        for l in range(len(temp)):
            temp[l] = float(temp[l])
        bandstructure[j, (k*8+12):] = temp

    frame = pd.DataFrame(bandstructure)

    return frame

if __name__ == "__main__":
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
        
    frame = nscf_scraper(input_file)
    frame.to_pickle(output_file)

