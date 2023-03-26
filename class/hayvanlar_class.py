class Hayvan():

    def __init__(self, hayvan_cinsi, hayvan_turu, hayvan_mensei, hayvan_aile, hayvan_yasam_suresi):
        self.hayvan_cinsi = hayvan_cinsi
        self.hayvan_turu = hayvan_turu
        self.hayvan_mensei = hayvan_mensei
        self.hayvan_aile = hayvan_aile
        self.hayvan_yasam_suresi = hayvan_yasam_suresi

print("Köpekler")
class Kopek(Hayvan):
    def __init__(self, hayvan_cinsi, hayvan_turu, hayvan_mensei, hayvan_aile, hayvan_yasam_suresi, hayvan_kilo, hayvan_boyutu, hayvan_asi):
        super().__init__(hayvan_cinsi, hayvan_turu, hayvan_mensei, hayvan_aile, hayvan_yasam_suresi)

        self.hayvan_kilo = hayvan_kilo
        self.hayvan_boyutu = hayvan_boyutu
        self.hayvan_asi = hayvan_asi

    def __str__(self):
        return "Hayvan cinsi : {}\nHayvan türü : {}\nHayvan menşei : {}\nHayvan ailesi : {}\nHayvan Yaşam Süresi : {}\nHayvan kilosu : {}\nHayvan boyutu : {}\nHayvan Aşısı : {}\n".format(self.hayvan_cinsi, self.hayvan_turu, self.hayvan_mensei, self.hayvan_aile, self.hayvan_yasam_suresi, self.hayvan_kilo, self.hayvan_boyutu, self.hayvan_asi)

kopek = Kopek("Köpek - Alaskan Klee Kai", "Arkadaş Köpek, Spitz Köpek", "Alaska", "Spitz, Northern", "13-16 yıl", "2-11kg", "30-43 cm", "Yapıldı")
print(kopek)


print("Kuşlar")
class Kus(Hayvan):
    def __init__(self, hayvan_cinsi, hayvan_turu, hayvan_mensei, hayvan_aile, hayvan_yasam_suresi, hayvan_boyutu):
        super().__init__(hayvan_cinsi, hayvan_turu, hayvan_mensei, hayvan_aile, hayvan_yasam_suresi)

        self.hayvan_boyutu = hayvan_boyutu

    def __str__(self):
        return "Hayvan cinsi : {}\nHayvan türü : {}\nHayvan menşei : {}\nHayvan ailesi : {}\nHayvan Yaşam Süresi : {}\nHayvan boyutu : {}\n".format(self.hayvan_cinsi, self.hayvan_turu, self.hayvan_mensei, self.hayvan_aile, self.hayvan_yasam_suresi, self.hayvan_boyutu)

kus = Kus("Kuş - Doğan Kerkenez", "Gündüz yırtıcı kuş", "Bilinmiyor", "Falconidae", "Bilinmiyor", "40-50 cm")
print(kus)


print("Atlar")
class At(Hayvan):
    def __init__(self, hayvan_cinsi, hayvan_turu, hayvan_mensei, hayvan_aile, hayvan_yasam_suresi, hayvan_bacaklari, hayvan_gebelik_suresi, yilda_kac_kere_doğum_yapar):
        super().__init__(hayvan_cinsi, hayvan_turu, hayvan_mensei, hayvan_aile, hayvan_yasam_suresi)

        self.hayvan_bacaklari = hayvan_bacaklari
        self.hayvan_gebelik_suresi = hayvan_gebelik_suresi
        self.yilda_kac_kere_doğum_yapar = yilda_kac_kere_doğum_yapar

    def __str__(self):
        return "Hayvan cinsi : {}\nHayvan türü : {}\nHayvan menşei : {}\nHayvan ailesi : {}\nHayvan Yaşam Süresi : {}\nHayvanın backları : {}\nHayvan kaç ay gebe kalır : {}\nHayvan yılda kaç kere doğum yapar : {}\n".format(self.hayvan_cinsi, self.hayvan_turu, self.hayvan_mensei, self.hayvan_aile, self.hayvan_yasam_suresi, self.hayvan_bacaklari, self.hayvan_gebelik_suresi, self.yilda_kac_kere_doğum_yapar)

at = At("At", "Arap atı", "Arap toprakları", "Arap", "25-30 yil", "Kuvvetli", "11-12ay", "Yılda 1 kere")
print(at)
