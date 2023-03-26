from sarki import *

print("""*************************

Şarkı Listesine Hoşgeldin

İşlemler:

1.Şarkı Listesini Göster
2.Şarkı Ekle
3.Şarkı Ara
4.Şarkı Listeden Sil

Çıkmak için q'ye basınız

*************************""")

sarki = SarkiKutuphane()

while True:
    islem = input("Bir işlem seçiniz: ")

    if (islem == "q"):
        print("Programl sonlandırıldı...")
        break
    
    elif (islem == "1"):
        sarki.sarkilar_goster()

    elif (islem == "2"):
        sarki_isim = input("Şarkı ismini giriniz: ")
        sanatci = input("Şarkı sanatçısını giriniz: ")
        album = input("Şarkı albümünü giriniz: ")
        pr_sirketi = input("Prodüksiyon şirketini giriniz: ")
        sarki_suresi = input("Şarkı süresini giriniz: ")

        yeni_sarki = Sarki(sarki_isim, sanatci, album, pr_sirketi, sarki_suresi)
        print("Şarkı ekleniyor...")
        time.sleep(2)
        sarki.sarki_ekle(yeni_sarki)
        print("Şarkı eklendi")

    elif (islem == "3"):
        sarki_isim = input("Hangi şarkıyı arıyorsunuz: ")
        print("Şarkı aranıyor...")
        time.sleep(2)
        sarki.sarki_sorgula(sarki_isim)

    elif (islem == "4"):
        sarki_isim = input("Hangi şarkıyı silmek istiyorsunuz: ")
        cevap = input("Emin misiniz(E/H): ")

        if (cevap == "E"):
            print("Şarkı siliniyor...")
            time.sleep(2)
            sarki.sarki_sil(sarki_isim)
            print("Şarkı silindi.")

    else:
        print("Geçersiz işlem girdiniz! Lütfen tekrar deneyin!")