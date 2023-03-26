"""
file = open("dosya_işlemleri/bilgiler.txt", "w", encoding="utf-8")
file.write("Abdullah Bahromov\nAbdurahmon Bahromov\nİbrahim Bahromov")
file.close()
"""

try:
    file = open("dosya_işlemleri/bilgiler.txt", "r", encoding="utf-8")
except FileNotFoundError:
    print("Dosya bulunamadı!")

for i in file:
    print(i, end="")   #print(i)
file.close()

