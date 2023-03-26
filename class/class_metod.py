class Kitap():
    
    def __init__(self, isim, yazar, sayfa_sayisi, kitap_turu):
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.kitap_turu = kitap_turu

    def __str__(self):
        return "Kitap ismi : {}\nKitap yazarı : {}\nKitap sayfası : {}\nKitap türü : {}".format(self.isim, self.yazar, self.sayfa_sayisi, self.kitap_turu)

    def __len__(self):
        return self.sayfa_sayisi

    def __del__(self):
        print("Kitap objesi siliniyor...")
    
    """
    def bilgileriGoster(self):
        print("Kitap ismi : {}\nKitap yazarı : {}\nKitap sayfası : {}\nKitap türü : {}".format(self.isim, self.yazar, self.sayfa_sayisi, self.kitap_turu))
    """

kitap = Kitap("İstanbul Harıtası", "Ahmet Ümit", 561, "Polisiye")
#kitap.bilgileriGoster()
print(kitap)
print(len(kitap))


"""
kitap = Kitap() ## __init__ metodu
print(kitap) ## __str__ metodu
"""