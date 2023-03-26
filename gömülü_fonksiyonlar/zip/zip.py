"""
Tanım ve Kullanım
Zip() işlevi, geçen her yineleyicideki ilk öğenin birlikte eşleştirildiği ve ardından her 
geçen yineleyicideki ikinci öğenin birlikte eşleştirildiği, vb. demetlerin bir yineleyicisi 
olan bir Zip nesnesi döndürür.

Geçilen yineleyicilerin farklı uzunlukları varsa, en az öğeye sahip yineleyici, yeni 
yineleyicinin uzunluğuna karar verir.

Syntax:
zip(iterator1, iterator2, iterator3 ...)
"""

liste1 = [1,2,3,4,5]
liste2 = [6,7,8,9,10]
liste3 = ["Python", "C#", "Java", "JS"]

i = 0
sonuc = list()

while (i < len(liste1) and i < len(liste2)):
    sonuc.append((liste1[i], liste2[i]))
    i += 1
print(sonuc)

print(zip(liste1, liste2))
print(list(zip(liste1, liste2)))

print(list(zip(liste1, liste2, liste3)))

for i, j in zip(liste1, liste3):
    print(i, j)

sozluk1 = {"Elma":1, "Armut":2, "Kiraz":3}
sozluk2 = {"Sıfır":0, "Bir":1, "İki":2}

print(list(zip(sozluk1, sozluk2)))
print(list(zip(sozluk1.values(), sozluk2.values())))