class kitap():
    ad = "harry potter"
    tür = "fantastik"
kitap1 = kitap()
print(kitap1.ad)
print(kitap1.tür)

############################

class ogrenci():
    ad = "Eren"
    soyad = "Yarar"
    bolumu = "Sayısal"

ogrenci1 = ogrenci()
print(ogrenci1.ad)
print(ogrenci1.soyad)
print(ogrenci1.bolumu)

############################

class Yazılımcı():

    def __init__(self, isim, soyisim, numara, maaş, diller):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara  # Yazılımcı objelerinin özellikleri
        self.maaş = maaş
        self.diller = diller

yazılımcı1 =  Yazılımcı("Mustafa Murat","Coşkun",12345,3000,["Python","C","Java"])

yazılımcı1.diller

############################

class Yazılımcı():

    def __init__(self, isim, soyisim, numara, maaş, diller):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara  # Yazılımcı objelerinin özellikleri
        self.maaş = maaş
        self.diller = diller
        
    def bilgileriGöster(self):
        print("""
        Çalışan Bilgisi:
        
        Ad: {}
        
        Soyad: {}
        
        numara: {}
        
        maaş: {}
        
        diller: {}
        
        
        
        """.format(self.ad,self.Soyad,self.numara,self.maaş,self.diller))
        
    def maasZam(self,yeni_maas):
        self.maaş += yeni_maas
        
yazılımcı1 = Yazılımcı("Eren","Yarar","444 1 44",3000,["java","Python","C#"])

yazılımcı1(bilgileriGöster())
yazılımcı1(maasZam(400))
yazılımcı1(bilgileriGöster())



