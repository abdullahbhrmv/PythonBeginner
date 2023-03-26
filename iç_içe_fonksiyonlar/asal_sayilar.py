"""
1'den 1000'e kadar olan asal sayıları ekrana yazdıran bir program yazın. 
Daha sonra bir tane decorator fonksiyon kullanarak bu fonksiyona 1'den 1000'e kadar 
olan mükemmel sayıları yazdırma özelliği ekleyin.
"""

def asal(a):
    b = 2
    if a == 1:
        return False
    elif a == 2:
        return True
    else:
        while b < a:
            if a % b == 0:
                return False
            b += 1
        return True
        
print(list(filter(asal, range(1, 1000))))