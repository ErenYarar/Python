################ Bilgileri Gösterme ######################
##########################################################

def bilgiler(ad="Bilgi yok",soyad="Bilgi yok",maas = 3000):
    print("Ad:",ad,"Soyad:",soyad,"maas:",maas)
bilgiler("Eren","Yarar")

##########################################################
###########  Fonksiyonlar ile İç içe çarpım  #############      
##########################################################

def uclecarp(a):
    print("1.fonksiyon çalıştı")
    return a*3

def ikiyletopla(a):
    print("2.fonksiyon çalıştı")
    return a+7

def besilecikar(a):
    print("3.fonksiyon çalıştı")
    return a-5

sayi = int(input("Sayı: "))
print(uclecarp(ikiyletopla(besilecikar(sayi))))






