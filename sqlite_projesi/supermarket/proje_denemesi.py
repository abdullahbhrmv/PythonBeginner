from supermarket import *

print("""*************************

Ürün Listesine Hoşgeldin

İşlemler:

1.Ürün Listesini Göster
2.Ürün Ekle
3.Ürün Ara
4.Ürün Listeden Sil

Çıkmak için q'ye basınız

*************************""")

urun = SuperMarket()

while True:
    islem = input("\nBir işlem seçiniz: ")

    if islem == "q":
        print("Programl sonlandırıldı...")
        break
    
    elif islem == "1":
        urun.urunler_goster()

    elif islem == "2":
        satici = input("\nSatıcısini girniz: ")
        urun_ismi = input("Ürün ismini giriniz: ")
        urun_markasi = input("Ürün markasını giriniz: ")
        urun_fiyat = input("Ürün fiyatını giriniz(tl): ")
        urun_gram = input("Ürün gramı giriniz(g): ")
        urun_puani = input("Ürün puanını giriniz: ")

        yeni_urun = Market(satici, urun_ismi, urun_markasi, urun_fiyat, urun_gram, urun_puani)
        print("Ürün ekleniyor. Bekleyiniz.")
        time.sleep(2)
        urun.urun_ekle(yeni_urun)
        print("Ürün başarılı bir şekilde eklendi")

    elif islem == "3":
        urun_ismi = input("Hangi ürünü arıyorsunuz: ")
        print("Ürün aranıyor...")
        time.sleep(2)
        urun.urun_sorgula(urun_ismi)

    elif islem == "4":
        urun_ismi = input("Hangi ürünü silmek istiyorsunuz: ")
        cevap = input("Emin misniz(E/H): ")

        if (cevap == "E"):
            print("Ürün siliniyor...")
            time.sleep(2)
            urun.urun_sil(urun_ismi)
            print("Ürün silindi.")

    else:
        print("Geçersiz işlem girdiniz! Lütfen tekrar deneyin!")