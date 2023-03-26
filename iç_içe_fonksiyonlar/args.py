def fonksiyon(*args):
    for i in args:
        print(i)
print(fonksiyon(1,2,3))

def fonksiyon1(isim, *args):
    print("İsim: ", isim)

    print("----------")
    for i in args:
        print(i)
print(fonksiyon1("Abdullah", 1,2,3,4,5))