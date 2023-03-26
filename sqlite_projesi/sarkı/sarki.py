"""
Siz de bir tane Şarkı projesi geliştirmeye çalışın.

                     Örnek özellikler;

                     1. Şarkı İsmi 
                     2. Sanatçı
                     3. Albüm
                     4. Prodüksiyon Şirketi
                     5. Şarkı Süresi

                     Örnek Metodlar;

                     1. Veritabanındaki Toplam Şarkı Süresini Hesaplayan Metod
                     2. Şarkı Ekle
                     3. Şarkı Sil
"""

import sqlite3
import time


class Sarki():
    def __init__(self, sarki_isim, sanatci, album, pr_sirketi, sarki_suresi):
        self.sarki_isim = sarki_isim
        self.sanatci = sanatci
        self.album = album
        self.pr_sirketi = pr_sirketi
        self.sarki_suresi = sarki_suresi
    
    def __str__(self):
        return "\nŞarkı ismi: {}\nŞarkı Sanatçısı: {}\nŞarkı Albümü: {}\nProdüksiyon Şirketi: {}\nŞarkı süresi: {}\n".format(self.sarki_isim, self.sanatci, self.album, self.pr_sirketi, self.sarki_suresi)


class SarkiKutuphane():
    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("sqlite\sarkilar.db")
        self.cursor = self.baglanti.cursor()

        sorgu = "Create Table If not exists şarkılar (sarki_isim TEXT, sanatci TEXT, album TEXT, pr_sirketi TEXT, sarki_suresi DOUBLE)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def baglanti_kes(self):
        self.baglanti.close()

    def sarkilar_goster(self):
        sorgu = "Select * From şarkılar"
        self.cursor.execute(sorgu)
        sarkilar = self.cursor.fetchall()

        if (len(sarkilar) == 0):
            print("Şarkı bulunamadı")
        else:
            for i in sarkilar:
                sarki = Sarki(i[0], i[1], i[2], i[3], i[4])
                print(sarki)

    def sarki_ekle(self, sarki):
        sorgu = "Insert into şarkılar Values(?, ?, ?, ?, ?)"
        self.cursor.execute(sorgu, (sarki.sarki_isim, sarki.sanatci, sarki.album, sarki.pr_sirketi, sarki.sarki_suresi))
        self.baglanti.commit()

    def sarki_sorgula(self, sarki_isim):
        sorgu = "Select * From şarkılar where sarki_isim = ?"
        self.cursor.execute(sorgu, (sarki_isim,))
        sarkilar = self.cursor.fetchall()

        if (len(sarkilar) == 0):
            print("Böyle bir şarkı bulunamadı")
        else:
            sarki = Sarki(sarkilar[0][0], sarkilar[0][1], sarkilar[0][2], sarkilar[0][3], sarkilar[0][4])
            print(sarki)

    def sarki_sil(self, sarki):
        sorgu = "Delete from şarkılar where sarki_isim = ?"
        self.cursor.execute(sorgu, (sarki,))
        self.baglanti.commit()