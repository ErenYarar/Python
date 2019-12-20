########### For döngüsü ###############

liste = [12,32,42,44,55,76]
toplam = 0

for i in liste:
    toplam += i
print("Toplam = ",toplam)

############  2.Ornek  ################


liste = [12,32,42,44,55,76]


for i in liste:
    if(i % 2 == 0):
        print("Çift sayılar = ",i)

############# 3.Ornek  ################

s = "Python"

for karakter in s:
    print(karakter * 3)

############# 4.Ornek  ################


liste = [(2,3),(4,5)]

for i,j in liste:
    print(i*j)
