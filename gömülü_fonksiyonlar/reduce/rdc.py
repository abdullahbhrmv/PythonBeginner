"""
Reduce(fun,seq) fonksiyonu, bağımsız değişkeninde geçirilen belirli bir işlevi, geçirilen 
dizide belirtilen tüm liste öğelerine uygulamak için kullanılır. Bu işlev, “functools” 
modülünde tanımlanır.

Çalışma :

1.İlk adımda dizinin ilk iki elemanı seçilir ve sonuç elde edilir.
2.Bir sonraki adım, aynı işlevi daha önce elde edilen sonuca uygulamaktır ve ikinci öğeyi hemen takip eden sayı ve sonuç yeniden depolanır.
3.Bu işlem kapta hiç eleman kalmayıncaya kadar devam eder.
4.Nihai döndürülen sonuç döndürülür ve konsolda yazdırılır.
"""

from functools import reduce

def toplama(x, y):
    return x + y

print(reduce(toplama, [12,18,20,10]))

print(reduce(lambda x, y : x * y, [1,2,3,4,5]))

def maksimum(x,y):
    if(x > y):
        return x
    else:
        return y
print(maksimum(3,4))

print(reduce(maksimum, [-2,3,1,4]))