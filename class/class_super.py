class Calisan():
    def __init__(self, isim, maas, departman):
        print("Çalışan sınıfının init fonksiyonu")

        self.isim = isim
        self.maas = maas
        self.departman = departman

    def bilgileriGoster(self):
        print("Çalışan sınıfının bilgileri...")

        print("İsim : {}\nMaaş : {}\nDepartman : {}\n".format(self.isim, self.maas, self.departman))

    def departmanDegistir(self, yeni_departman):
        self.departman = yeni_departman


class Yonetici(Calisan):
    def __init__(self, isim, maas, departman, kisi_sayisi):
        super().__init__(isim, maas, departman)
                
        print("Yönetici sınıfının init fonksiyonu")
        self.kisi_sayisi = kisi_sayisi

    def bilgileriGoster(self):
        print("Yönetici sınıfının bilgileri...")

        print("İsim : {}\nMaaş : {}\nDepartman : {}\nSorumlu Kişi Sayısı : {}".format(self.isim, self.maas, self.departman, self.kisi_sayisi))
        
    def zamYap(self, zam_miktari):
        self.maas += zam_miktari

yonetici = Yonetici("Abdurahmon Bahromov", 10000, "İnşaat", 10)
yonetici.bilgileriGoster()