"""
Problem 1
Elinizde stringlerin bulunduğu bir liste bulunduğunu düşünün.

liste = ["345","sadas","324a","14","kemal"]

Bu listenin içindeki stringlerden içinde sadece rakam bulunanları ekrana yazdırın. Bunu yaparken try,except bloklarını kullanmayı unutmayın.
"""
liste = ["345","sadas","324a","14","kemal"]

for eleman in liste:
    try:
        sayi = int(eleman)
        print(sayi)
    except ValueError:
        pass

"""
Problem 2
Bir sayının çift olup olmadığını sorgulayan bir fonksiyon yazın. Bu fonksiyon, eğer sayı 
çift ise *return* ile bu değeri dönsün. Ancak sayı tek sayı ise fonksiyon *raise* ile 
*ValueError* hatası fırlatsın. Daha sonra, içinde çift ve tek sayılar bulunduran bir liste 
tanımlayın ve liste üzerinde gezinerek ekrana sadece çift sayıları bastırın.

"""

def cift_sayi_mi(sayi):
    if sayi % 2 == 0:
        return sayi
    else:
        raise ValueError("Tek sayı hatası!")

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for sayi in liste:
    try:
        print(cift_sayi_mi(sayi))
    except ValueError:
        pass
