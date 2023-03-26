def fonksiyon(**kwargs):
    print(kwargs)
print(fonksiyon(isim = "Abdullah", soyisim = "Bahromov", numara = 12345))

def fonksiyon(**kwargs):
    for i, j in kwargs.items():
        print("Argüman ismi: ", i, "\t", "Argüman Değeri: ", j)
print(fonksiyon(isim = "Abdullah", soyisim = "Bahromov", numara = 12345))
