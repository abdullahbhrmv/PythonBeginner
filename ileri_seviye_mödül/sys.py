import sys

#print(dir(sys))
"""
a = int(input("a: "))
b = int(input("b: "))

sys.exit()  # Bundan sonraki satırlar(yazılan kodlar) çalışmaz

c = int(input("c: "))
"""
"""
sys.stderr.write("Bu bir hata mesajıdır\n")
sys.stderr.flush()

sys.stdout.write("Bu normal mesajdır\n")

print(sys.argv)
"""

for i in sys.argv:
    print(i)