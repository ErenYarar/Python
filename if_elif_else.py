#############  İşlem secme ###################

islem = int(input("islem secin: "))

if(islem == 1):
    print("1.islemi sectiniz...")
elif(islem == 2):
    print("2.islemi sectiniz...")
elif(islem == 3):
    print("3.islemi sectiniz...")
else:
    print("Gecersiz islem")


##############################################

############  Mekan Girişi (Yaş)  ############

##############################################


yas = int(input("yasını gir: "))

if(yas < 18):
    if(yas < 0 ):
        print("-'li yaşlarda olamazsınız.")
    print("Mekana giremezsin...")
elif(yas >= 18):
    if(yas > 110):
        print("Bu yaşlarda olamazsınız..Tekrar deneyin..")
    print("Hosgeldiniz...")

##############################################

############     Harf Notu        ############

##############################################

while True:

    note = float(input("Notunuzu giriniz:"))

    if note >= 90:
        print("AA")
    elif note >= 85:
        print("BA")
    elif note >= 90:
        print("BA")
    elif note >= 80:
        print("BB")
    elif note >= 75:
        print("CB")
    elif note >= 70:
        print("CC")
    elif note >= 65:
        print("DC")
    elif note >= 60:
        print("DD")
    else:
        print("Dersten Kaldınız")


