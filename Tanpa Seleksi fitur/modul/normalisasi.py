from json import load
from nltk.tokenize import TweetTokenizer
import re
import os
dir_path = os.path.dirname(os.path.realpath(__file__))


def reduksi_huruf(kata):
    nkata  = list()
    for i,k in enumerate(kata):
        if i>2:
            if kata[i]== kata[i-1] and kata[i] == kata[i-2]:
                continue
            else:
                nkata.append(k)
        else:
            nkata.append(k)
    return "".join(nkata)

with open(dir_path+'/data.json', 'r') as f:
    data = load(f)

tknzr = TweetTokenizer()
def normalisasi (kalimat):
    kalimat = tknzr.tokenize(kalimat.lower())

    #reduksi huruf
    for idx, i in enumerate(kalimat):
        kalimat[idx] = reduksi_huruf(i)

    #Normalisasi kata
    for i, k in enumerate(kalimat):
        if k in data['hapus']:
            kalimat[i] = ""
        elif k in data['ganti']:
            kalimat[i] = data['ganti'][k]
    kalimat = " ".join(kalimat).strip()
    return re.sub(' +', ' ', kalimat.lstrip().rstrip())