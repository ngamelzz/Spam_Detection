from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

import pandas as pd


def data_separate(y, complement=False):
    kelas = sorted(set(y))
    dict_index = dict()
    for c in kelas:
        index = list()
        for ix, c_ in enumerate(y):
            if complement==False and c==c_:
                index.append(ix)
            elif complement==True and c!=c_:
                index.append(ix)
        dict_index.update({c:index})
    return dict_index

class ChiSquare:
    def __init__(self, alpha = 0.001):
        self.alpha = alpha

        self.nilai_kritis = {
            0.1   : 2.71,
            0.05 : 3.84,
            0.01 : 6.63,
            0.005 : 7.88,
            0.001 : 10.83
        }

        if self.alpha not in self.nilai_kritis:
            print(self.alpha, "tidak termasuk dalam tabel nilai kritis")

    def find_best_features(self, data, label, fitur = None):

        if fitur == None:
            vectorizer = CountVectorizer(binary=True)
        else:
            vectorizer = CountVectorizer(vocabulary = fitur, binary=True)

        X = vectorizer.fit_transform(data)
        nchi = X.shape[0]
        self.fitur = vectorizer.get_feature_names()
        index_doc = data_separate(label)
        index_doc_complement = data_separate(label, complement=True)

        self.classes = list(set(label))

        self.dict_chis = {"fitur":self.fitur}
        # for c_ in list(reversed(self.classes)):
        for c_ in self.classes:
            A = np.sum(X[index_doc[c_]], axis=0).A
            B = X[index_doc[c_]].shape[0] - A

            C = np.sum(X[index_doc_complement[c_]], axis=0).A
            D = X[index_doc_complement[c_]].shape[0] - C

            AD = A*D
            CB = C*B

            atas = nchi * (AD - CB)**2
            bawah = (A + C) * (B + D) * (A + B) * (C + D)
            x_pangkat2 = atas/bawah
            # print(atas, bawah)
            self.dict_chis.update({c_:list(x_pangkat2[0])})
            # print(A, B, C, D, "| ")
            # print("=================================================")
        self.best_features = list()
        nk = self.nilai_kritis[self.alpha]
        # print(self.dict_chis[self.classes[0]])
        for term, sp, nsp in zip(self.fitur, self.dict_chis[self.classes[0]], self.dict_chis[self.classes[1]]):
            # print(sp, nsp)
            if sp>=nk or nsp>=nk:
                self.best_features.append(term)

        self.data = pd.DataFrame.from_dict(self.dict_chis)