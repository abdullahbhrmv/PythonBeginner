"""
Genellikle, yineleyicilerle uğraşırken, yineleme sayısını da tutmamız gerekir. 
Python, bu görev için yerleşik bir enumerate() işlevi sağlayarak programcıların görevini 
kolaylaştırır. Enumerate() yöntemi, yinelenebilir bir değere bir sayaç ekler ve onu 
numaralandırma nesnesi biçiminde döndürür. Bu numaralandırılmış nesne daha sonra doğrudan 
döngüler için kullanılabilir veya list() işlevi kullanılarak bir demet listesine 
dönüştürülebilir.

Syntax:
enumerate(iterable, start=0)
"""

liste = ["elma", "armut", "kiraz", "muz", "kivi"]

i = 0
sonuc = list()

while (i < len(liste)):
    sonuc.append((i, liste[i]))
    i += 1
print(sonuc)

#enumerate
enumerate(liste)
print(list(enumerate(liste)))

for i,j in enumerate(liste):
    print(i,j)
