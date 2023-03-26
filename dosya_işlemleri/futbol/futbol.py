import random

futbolcular = ["Altay Bayindir, Fenerbahçe",
               "Attila Szalai, Fenerbahçe",
               "Serdar Aziz, Fenerbahçe",
               "Ferdi Kadioglu, Fenerbahçe",
               "Arda Güler, Fenerbahçe",
               "Enner Valencia, Fenerbahçe",
               "Mauro İcardi, Galatasaray",
               "Fernando Muslera, Galatasaray",
               "Kerem Aktürköğlü, Galatasaray",
               "Dries Mertens, Galatasaray",
               "Juan Mata, Galatasaray",
               "Yusuf Demir, Galatasaray",
               "Dele Alli, Beşiktaş",
               "Rachid Ghezzal, Beşiktaş",
               "Nathan Redmond, Beşiktaş",
               "Cenk Tosun, Beşiktaş",
               "Jackson Muleka, Beşiktaş",
               "Tayfun Bingöl, Beşiktaş"]

with open("dosya_işlemleri/futbol/futbolcular.txt", "w", encoding="utf-8") as file1:
    
    for futbolcu in futbolcular:
        file1.write(futbolcu + "\n")

with open("dosya_işlemleri/futbol/futbolcular.txt", "r", encoding="utf-8") as file2:
    
    fb_oyunculari = []
    gs_oyunculari = []
    bjk_oyunculari = []

    for satir in file2:
        satir = satir[:-1]
        takim = satir.split(",")

        if takim[1] == "Galatasaray":
            gs_oyunculari.append(satir + "\n")
        elif takim[1] == "Fenerbahçe":
            fb_oyunculari.append(satir + "\n")
        else:
            bjk_oyunculari.append(satir + "\n")

    with open("dosya_işlemleri/futbol/gs.txt", "w", encoding="utf-8") as file3:
        
        for futbolcu in gs_oyunculari:
            file3.write(futbolcu)
    
    with open("dosya_işlemleri/futbol/fb.txt", "w", encoding="utf-8") as file4:
        
        for futbolcu in fb_oyunculari:
            file4.write(futbolcu)

    with open("dosya_işlemleri/futbol/bjk.txt", "w", encoding="utf-8") as file5:
        
        for futbolcu in bjk_oyunculari:
            file5.write(futbolcu)
