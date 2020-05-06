from bs4 import BeautifulSoup
import codecs


def get_comments(nama_file):
    panjang_komentar = list()
    file = codecs.open(nama_file, "r", "utf-8")
    doc = file.read()
    soup = BeautifulSoup(doc, 'html.parser')
    komentar_list = soup.findAll("div","C4VMK")
    
    komentar_ = list()
    for i in komentar_list:
        i = i.find("span")
        if i.get_text() not in komentar_ and i.get_text() != "Sudah Diverifikasi":
            komentar_.append(i.get_text())
            panjang_komentar.append(len(i.get_text().split()))
    return panjang_komentar, komentar_
