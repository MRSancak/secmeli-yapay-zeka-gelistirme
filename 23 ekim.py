#değişkenler
ad="Hamdican"
yas=16
ehliyet=False
kilo=68.5

#type kodu değişkenin türünü söyler
print(type(ad))
print(type(yas))
print(type(ehliyet))
print(type(kilo))

#string ifadelerin yanında değişken koyma
print("benimadım:",ad)
print("kilom:",kilo)
print("yaşım:",yas)
print("ehliyet durumum:",ehliyet)

#listeler
ogrenci=[35,"Merhaba","elma",11,"Armut"] #liste 
#liste sırası 0 dan başlar
print(type(ogrenci)) #liste tipi
print(len(ogrenci)) #eleman miktarı
ogrenci.append("Toki") #listeye ekleme sonuna
print(ogrenci)
ogrenci.insert(2,"Hamdi") #sıraya göre ekleme
print(ogrenci)
ogrenci.remove("Hamdi") #silme
print(ogrenci)
ogrenci.pop(2) # 2. indextekini silme
print(ogrenci)
