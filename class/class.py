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
    def zamYap(self, zam_miktari):
        self.maas += zam_miktari

yonetici = Yonetici("Abdullah Bahromov", 10000, "Yazılım")
yonetici.bilgileriGoster()

yonetici.departmanDegistir("Bilişim")
yonetici.bilgileriGoster()

yonetici = Yonetici("İbrahim Bahromov", 10000, "Oyun")
yonetici.zamYap(1500)
yonetici.bilgileriGoster()
