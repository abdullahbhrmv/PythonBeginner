"""def fonksiyon(islem_adi):
    
    def toplama(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam
        
    def carpma(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpim
    
    if islem_adi == "toplama":
        return toplama
    else:
        return carpma

deneme = fonksiyon("toplama")
print(deneme(1,2,3,4,5))"""

def toplama(a,b):
    return a + b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a * b
def bolme(a,b):
    return a / b

def anafonksiyon(func1,func2,func3,func4,islem_adi): # Tanımladığımız 4 fonksiyonu da argüman olarak göndereceğiz.
    if (islem_adi == "toplama"):
        print(func1(3, 4))
    elif (islem_adi == "çıkarma"):
        print(func2(10, 3))
    elif (islem_adi == "çarpma"):
        print(func3(10, 3))
    elif (islem_adi == "bölme"):
        print(func4(10, 4))
    else:
        print("Geçersiz işlem adı...")

print(anafonksiyon(toplama, cikarma, carpma, bolme, "toplama"))
print(anafonksiyon(toplama, cikarma, carpma, bolme, "çıkarma"))
print(anafonksiyon(toplama, cikarma, carpma, bolme, "çarpma"))
print(anafonksiyon(toplama, cikarma, carpma, bolme, "bölme"))