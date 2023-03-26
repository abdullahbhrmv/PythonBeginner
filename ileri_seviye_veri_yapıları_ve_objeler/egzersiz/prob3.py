"""
Elinizde "mailler.txt" adında , maillerin ve bazı yazıların bulunduğu bir dosya olsun. Bu dosyanın her bir satırını okuyun ve sadece mail formatına uygun olanları ekrana yazdırın.

                    coskun.m.murat@gmail.com
                    example@xyz.com
                    mustafa.com
                    mustafa@gmail
                    kerim@yahoo.com

                           //
                           //
                           //


*İpucu: Stringlerde bulunan endswith ve find metodlarını kullanabilirsiniz.*
"""

with open("ileri seviye veri yapıları ve objeler\egzersiz\mailler.txt", "r", encoding="utf-8") as file:
    for i in file:
        i = i.strip()
        if i.endswith(".com") and "@" in i and i.find("@") < i.find(".com"):
            print(i)