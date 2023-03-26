from kutuphane import *

print("""****************

Kütüphaneye Hoşgeldiniz.

İşlemler:

1. Kitapları göster
2. Kitap Sorgula
3. Kitap Ekle
4. Kitap Sil
5. Kitap Baskisı Yükselt

Çıkmak için q'ye basınız

****************""")

kutuphane = Kutuphane()

while True:
    islem = input("Bir işlem seçiniz: ")

    if (islem == "q"):
        print("Program sonlandırılıyor...")
        break

    elif (islem == "1"):
        kutuphane.kitaplar_goster()

    elif (islem == "2"):
        isim = input("Hangi kitabı istiyorsunuz: ")
        print("Kitap sorgulanıyor...")
        time.sleep(2)

        kutuphane.kitap_sorgula(isim)

    elif (islem == "3"):
        isim = input("Kitap ismini giriniz: ")
        yazar = input("Yazar ismini giriniz: ")
        yayinevi = input("Yayinevini giriniz: ")
        tur = input("Kitap türünü giriniz: ")
        baski = int(input("Kitap baskısını giriniz: "))

        yeni_kitap = Kitap(isim, yazar, yayinevi, tur, baski)

        print("Kitap ekleniyor...")
        time.sleep(2)

        kutuphane.kitap_ekle(yeni_kitap)
        print("Kitap eklendi.")

    elif (islem == "4"):
        isim = input("Hangi kitabı silmek istiyormusunuz: ")
        cevap = input("Emin misiniz(E/H): ")
        
        if (cevap == "E"):
            print("Kitap siliniyor...")
            time.sleep(2)
            kutuphane.kitap_sil(isim)
            print("Kitap silindi.")

    elif (islem == "5"):
        isim = input("Hangi kitabın baskısını yükseltmek istiyorsunuz: ")
        print("Baskı yükseltiliyor...")
        time.sleep(2)
        kutuphane.baski_yukselt(isim)
        print("Baskı yükseltildi.")

    else:
        print("Geçersiz işlem girdiniz! Lütfen tekrar deneyin!")