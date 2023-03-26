"""
Elinizde uzunca bir string olsun.

            "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"


Bu string içindeki harflerin frekansını (bir harfin kaç defa geçtiği) bulmaya çalışın.

*İpucu : Kodlama egzersizimizde buna çok benzer bir şey yapmıştık.*
"""

s = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"

frekanslar = {}

for harf in s:
    if harf in frekanslar:
        frekanslar[harf] += 1
    else:
        frekanslar[harf] = 1

print(frekanslar)