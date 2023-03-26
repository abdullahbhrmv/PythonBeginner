"""
filter() yöntemi, dizideki her öğenin doğru olup olmadığını test eden bir işlev yardımıyla 
verilen diziyi filtreler.

syntax:

filtre(işlev, sıra)
Parameters:
işlev: bir öğenin her bir öğesinin test edilip edilmediğini test eden işlev
sıra doğru ya da değil.
sıra: filtrelenmesi gereken sıra, olabilir
herhangi bir yineleyicinin kümeleri, listeleri, demetleri veya kapsayıcıları olabilir.
Returns:
zaten filtrelenmiş bir yineleyici döndürür.
"""


print(filter(lambda x : x % 2 == 0, [1,2,3,4,5,6,7,8]))

print(list(filter(lambda x : x % 2 == 0, [1,2,3,4,5,6,7,8])))

def asalmi(x):
    i = 2
    if (x == 1):
        return False
    elif (x == 2):
        return True
    else:
        while (i < x):
            if (x % i == 0):
                return False
            i += 1
        return True

print(asalmi(5))
print(asalmi(1))
print(asalmi(2))

print(list(filter(asalmi, range(1, 100))))