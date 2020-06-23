import pandas as pd
from unidecode import unidecode

import os
import re
# from numba import cuda
dir_path = os.path.dirname(os.path.realpath(__file__))

fo = pd.read_excel(dir_path + '/' +'data/karakter.xlsx', sheet_name='Sheet1')
x = fo['karakter'].tolist() #
y = fo['replace'].tolist()
def gantiKarakter(str, x=x, y=y):
    for i in range(len(x)):
        if i == 0:
            n_word = str
        n_word = n_word.replace(x[i],y[i])
    return unidecode(n_word).lower()


def NormalisasiKarakter(str, x=x, y=y):
    for i in range(len(x)):
        if i == 0:
            n_word = str
        n_word = n_word.replace(x[i],y[i])
    return unidecode(n_word).lower()