import random as r


rastgele_sayi = r.randint(1,100)
hak = 3

while True:
    tahmin = int(input("sayınızı girin: "))

    if(tahmin == rastgele_sayi):
        print("Tebrikler..Bildiniz")
        print("Sayı: ",rastgele_sayi)
        print("Hak: ", hak)
    elif(rastgele_sayi > tahmin):
        print("Maalesef..Bilemedin")
        print("Daha yüksek sayı seç")
        hak -= 1
        print("Kalan Hakkınız: ", hak)

    elif (rastgele_sayi < tahmin):
        print("Maalesef..Bilemedin")
        print("Daha alçak sayı seç")
        hak -= 1
        print("Kalan Hakkınız: ", hak)

    else:
        print("Geçersiz Sayı girdin...")


    if(hak == 0):
        print("Hakkınız bitmiştir...")
        print("Sayımız: ", rastgele_sayi)
        break
