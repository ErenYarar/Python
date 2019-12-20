def tambolen(sayi):
    tam_bolen = []

    for i in range(2,sayi):
        if(sayi % i == 0):
            tam_bolen.append(i)
    return tam_bolen

while True:
    sayi = input("sayi: ")

    if(sayi == "q"):
        print("Kapatılıyor...")
        break

    else:
        sayi = int(sayi)
        print("tam bölen: ",tambolen(sayi))
