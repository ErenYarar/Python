sayi1 = int(input("Sayı: "))
sayi2 = int(input("Sayı: "))

fibonacci = [sayi1 , sayi2]

for i in range(10):

    sayi1 , sayi2 = sayi2 , sayi1 + sayi2
    fibonacci.append(sayi2)

print("fibonacci:", fibonacci)
