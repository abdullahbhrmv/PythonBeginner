"""
Any ve All, ardışık And/Or için kullanılan, python'da sağlanan iki yerleşik işlevdir. 
Any Öğelerden herhangi biri True ise true değerini döndürür. Boşsa veya tümü yanlışsa False
döndürür. Herhangi biri, sağlanan yinelemeler üzerinde bir OR işlemleri dizisi olarak 
düşünülebilir. Yürütmede kısa devre yapar, yani sonuç öğrenilir öğrenilmez yürütmeyi durdurur.
"""

def hepsi(liste):
    for i in liste:
        if not i:
            return False
    return True

liste = [True, True, False, True]
print(hepsi(liste))
liste = [True, True, True, True]
print(hepsi(liste))
liste = [1,2,3,4,5]
print(hepsi(liste))

def herhangi(liste):
    for i in liste:
        if i:
            return True
    return False

liste = [True, True, False, True]
print(herhangi(liste))
liste = [0,0,0,0,0]
print(herhangi(liste))

# All ve Any
liste = [True, True, False, True]
print(all(liste))
print(all([True, True, True, True]))

print(any([True, True, False, True]))

