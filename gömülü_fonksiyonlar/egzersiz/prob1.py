"""
Elinizde bir dikdörtgenin kenarlarını ifade eden sayı çiftlerinin bulunduğu bir liste olsun.

         [(3,4),(10,3),(5,6),(1,9)]

Şimdi kenar uzunluklarına göre dikdörtgenin alanını hesaplayan bir fonksiyon yazın ve bu 
listenin her bir elemanına bu fonksiyonu uygulayarak ekrana şöyle bir liste yazdırın.

         [12, 30, 30, 9]

*Not : map() fonksiyonunu kullanmaya çalışın.*
"""

def diktortgen_alani(a, b):
    return a * b

kenarlar = [(3,4),(10,3),(5,6),(1,9)]

alanlari = list(map(lambda x : diktortgen_alani(x[0], x[1]), kenarlar))
print(alanlari)