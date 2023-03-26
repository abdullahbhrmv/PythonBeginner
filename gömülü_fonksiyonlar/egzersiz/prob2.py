"""
Elinizden her bir elemanı 3'lü bir demet olan bir liste olsun.

     [(3,4,5),(6,8,10),(3,10,7)]

Şimdi kenar uzunluklarına göre bu kenarların bir üçgen olup olmadığını 
dönen bir fonksiyon yazın ve sadece üçgen belirten kenarları bulunduran listeyi 
ekrana yazdırın.

     [(3, 4, 5), (6, 8, 10)]

*** Not: filter() fonksiyonunu kullanmaya çalışın. ***
"""

def ucgen(kenar):
    a, b, c = sorted(kenar)
    return a + b > c

kenarlar = [(3,4,5),(6,8,10),(3,10,7)]
sonuc = list(filter(ucgen, kenarlar))
print(list(sonuc))

"""
sorted()

Tanım ve Kullanım
sorted() işlevi, belirtilen yinelenebilir nesnenin sıralanmış bir listesini döndürür.

Artan veya azalan düzen belirleyebilirsiniz. Dizeler alfabetik olarak sıralanır ve sayılar 
sayısal olarak sıralanır.

Syntax:
sorted(iterable, key=key, reverse=reverse)
"""