with open("dosya_işlemleri/bilgiler.txt", encoding="utf-8") as file:
    print(file.tell)
    file.seek(20)
    print("file.tell()")