"""
Süpermarket içindeki ürünler üzerinden bir tane Süpermarket Projesi geliştirmeye çalışın.
"""

import sqlite3
import time

class Market():
    def __init__(self, satici, urun_ismi, urun_markasi, urun_fiyat, urun_gram, urun_puani):
        self.satici = satici
        self.urun_ismi = urun_ismi
        self.urun_markasi = urun_markasi
        self.urun_fiyat = urun_fiyat
        self.urun_gram = urun_gram
        self.urun_puani = urun_puani

    def __str__(self):
        return "\nSatıcı: {}\nÜrün: {}\nÜrün Markası: {}\nÜrün Fiyatı(tl): {}\nÜrün Gramajı(g): {}\nÜrün Puanı: {}\n".format(self.satici, self.urun_ismi, self.urun_markasi, self.urun_fiyat, self.urun_gram, self.urun_puani)


class SuperMarket():
    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("sqlite\supermarket.db")
        self.cursor = self.baglanti.cursor()

        sorgu = "Create Table If not exists urunler (satici TEXT, urun_ismi TEXT, urun_markasi TEXT, urun_fiyat DOUBLE, urun_gram DOUBLE, urun_puani DOUBLE)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def baglanti_kes(self):
        self.baglanti.close()

    def urunler_goster(self):
        sorgu = "Select * From  urunler"
        self.cursor.execute(sorgu)
        urunler = self.cursor.fetchall()

        if len(urunler) == 0:
            print("Ürün Bulunamadı")
        else:
            for i in urunler:
                urun = Market(i[0], i[1], i[2], i[3], i[4], i[5])
                print(urun)

    def urun_ekle(self, urun):
        sorgu = "Insert into urunler Values(?, ?, ?, ?, ?, ?)"
        self.cursor.execute(sorgu, (urun.satici, urun.urun_ismi, urun.urun_markasi, urun.urun_fiyat, urun.urun_gram, urun.urun_puani))
        self.baglanti.commit()

    def urun_sorgula(self, urun_ismi):
        sorgu = "Select * From urunler where urun_ismi = ?"
        self.cursor.execute(sorgu, (urun_ismi,))
        urunler = self.cursor.fetchall()

        if (len(urunler) == 0):
            print("Böyle bir ürün bulunamadı")
        else:
            urun = Market(urunler[0][0], urunler[0][1], urunler[0][2], urunler[0][3], urunler[0][4], urunler[0][5])
            print(urun)

    def urun_sil(self, urun):
        sorgu = "Delete from şarkılar where urun_ismi = ?"
        self.cursor.execute(sorgu, (urun,))
        self.baglanti.commit()
