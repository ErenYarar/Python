import time as t


kullanici_adi = "erenyarar"
sifre = "1234"

hak = 5

while True:
    giris = input("Kullanici adinizi giriniz: ")
    parola = input("Sifrenizi giriniz: ")

    islem = input("Kapatmak için 'q' ya basın...")

    if(islem == "q"):
        print("Kapatılıyor...")
        t.sleep(1)
        break
    elif(kullanici_adi == giris and parola == sifre):
        print("Hosgeldiniz")
        break
    elif (kullanici_adi != giris and parola == sifre):
        print("Kullanıcı adınızı yanlış girdiniz..")
        hak -= 1
        print("Kalan Hakkınız: ",hak)
    elif (kullanici_adi == giris and parola != sifre):
        print("Sifrenizi yanlış girdiniz..")
        hak -= 1
        print("Kalan Hakkınız: ", hak)

    elif (kullanici_adi != giris and parola != sifre):
        print("Kullanıcı adınızı ve Sifrenizi yanlış girdiniz..")
        hak -= 1
        print("Kalan Hakkınız: ", hak)

    if(hak == 0):
        print("Hakkınız bitmiştir...")
        break
