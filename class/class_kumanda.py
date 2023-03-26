import random
import time

class Kumanda():

    def __init__(self, tv_durumu = "Kapalı", tv_ses = 0, kanal_listesi = ["Trt"], kanal = "Trt"):
        self.tv_durumu = tv_durumu
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal


    def tvAc(self):
        
        if(self.tv_durumu == "Açık"):
            print("Televizyon açık!")
        else:
            print("Televizyon açılıyor...")
            self.tv_durumu = "Açık"

    def tvKapat(self):

        if(self.tv_durumu == "Kapalı"):
            print("Televizyon kapalı!")
        else:
            print("Televizyon kapatılıyor...")
            self.tv_durumu = "Kapalı"

    def sesAyarlari(self):
        
        while True:
            cevap = input("Sesi azaltmak için : '<'\nSesi artırmak için : '>'\nÇıkış için çıkış yazınız\nİşlem giriniz : ")

            if (cevap == "<"):
                if (self.tv_ses != 0):
                    self.tv_ses -= 1
                    print("Ses: ", self.tv_ses)
            
            elif (cevap == ">"):
                if(self.tv_ses != 100):
                    self.tv_ses += 1
                    print("Ses: ", self.tv_ses)

            else:
                print("Ses güncellendi: ", self.tv_ses)
                break

    def kanalEkle(self, kanal_ismi):
        
        print("Kanal ekleniyor...")
        time.sleep(1)

        self.kanal_listesi.append(kanal_ismi)
        print("Kanal eklendi!")

    def rastgeleKanal(self):
        rastgele = random.randint(0, len(self.kanal_listesi)-1)

        self.kanal = self.kanal_listesi[rastgele]
        print("Şu anki Kanal: ", self.kanal)

    def __len__(self):
        return len (self.kanal_listesi)

    def __str__(self):
        return "Tv durumu : {}\nTv ses : {}\nKanal listesi : {}\nŞu anki kanal : {}\n".format(self.tv_durumu, self.tv_ses, self.kanal_listesi, self.kanal)


kumanda = Kumanda()

print("""

Televizyon uygulaması

1. Tv aç
2. Tv kapat
3. Ses ayarları
4. Kanal ekle
5. Kanal sayısı
6. Rastgele Kanal
7. Televizyon bilgileri

Çıkmak için 'q' ya basın

""")


while True:
    islem = input("İşlem seçiniz: ")

    if(islem == "q"):
        print("Program sonlandırıldı!")
        break

    elif (islem == "1"):
        kumanda.tvAc()

    elif (islem == "2"):
        kumanda.tvKapat()

    elif (islem == "3"):
        kumanda.sesAyarlari()
    
    elif (islem == "4"):
        kanal_isimleri = input("Kanal isimlerini ','  ile ayırarak girin: ")
        kanal_listesi = kanal_isimleri.split(",")
        for eklencekler in kanal_listesi:
            kumanda.kanalEkle(eklencekler)

    elif (islem == "5"):
        print("Kanal sayısı: ", len(kumanda))

    elif (islem == "6"):
        kumanda.rastgeleKanal()

    elif (islem == "7"):
        print(kumanda)

    else:
        print("Geçersiz işlem girdiniz!")
