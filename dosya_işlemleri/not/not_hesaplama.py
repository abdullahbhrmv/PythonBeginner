def notHesapla(satir):
    satir = satir[:-1]
    
    liste = satir.split(",")
    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])

    son_not = not1 * (3/10) + not2 * (3/10) + not3 * (4/10)

    if son_not >= 90:
        harf = "AA"
    elif son_not >= 85:
        harf = "BA"
    elif son_not >= 80:
        harf = "BB"
    elif son_not >= 75:
        harf = "CB"
    elif son_not >= 70:
        harf = "CC"
    elif son_not >= 65:
        harf = "DC"
    elif son_not >= 60:
        harf = "DD"
    else:
        harf = "FF"

    return isim + "---------------------->" + harf + "\n"


with open("dosya_işlemleri/dosya.txt", "r", encoding="utf-8") as file:

    eklenecekler_listesi = []
    kalanlar_listesi = []
    gecenler_listesi = []

    for i in file:
        not_hesapla = notHesapla(i)
        not_hesapla2 = notHesapla(i)
        eklenecekler_listesi.append(notHesapla(i))

        if "FF" in not_hesapla:
            kalanlar_listesi.append(not_hesapla)
        else:
            gecenler_listesi.append(not_hesapla2)

    with open("dosya_işlemleri/notlar.txt", "w", encoding="utf-8") as file2:

        for i in eklenecekler_listesi:
            file2.write(i)

    with open("dosya_işlemleri/kalanlar.txt", "w", encoding="utf-8") as file3:
        
        for i in kalanlar_listesi:
            file3.write(i)

    with open("dosya_işlemleri/geçenler.txt", "w", encoding="utf-8") as file4:

        for i in gecenler_listesi:
            file4.write(i)
