sayi = int(input("Sayı: "))

faktoriyel = 1

for i in range(2,sayi+1):
    faktoriyel *= i

print("Faktoriyel: ",faktoriyel)
