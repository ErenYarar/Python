import time as t

print("********************\nATM sistemine hoşgeldiniz\n********************")
print("""
    İşlemler:
             Bakiye sorgulama: 1
             Para eklemek için: 2
             Para çekmek için: 3
             Hesapdan çıkmak için: 0 """)


bakiye = 1000 # Bakiyemiz 1000 lira olsun.


while True:
    islem = input("İşlem seçiniz: ")
    if(islem == 0):
        print("Hesapdan çıkılıyor...")
        t.sleep(1)
        print("Yine bekleriz....")
        break
    elif(islem == 1):
        print("Bakiyeniz sorgulanıyor...")
        t.sleep(1)
        print("Bakiyeniz: {}".format(bakiye))
    elif(islem == 2):
        miktar = int(input("Miktar giriniz: "))
        if(miktar > 3000):
            print("3000 den fazla para ekleyemezsiniz...")
        print("Bakiyenize para ekleniyor...")
        t.sleep(1)
        bakiye += miktar
        print("Paranız eklendi: {}".format(bakiye))
    elif (islem == 3):
        miktar = int(input("Miktar giriniz: "))
        if(bakiye - miktar < 0):
            print("Bakiye sınırını aştınız!")
            print("Bakiyeniz: {}".format(bakiye))
            continue
        print("Bakiyenizden para çekiliyor...")
        t.sleep(1)
        bakiye -= miktar
        print("Paranız çekildi: {}".format(bakiye))

    else:
        print("Gecersiz islem...")




