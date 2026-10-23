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
ogrenci=[35,"Merhaba","elma",11,"Armut",True] #liste 
#liste sırası 0 dan başlar
print(type(ogrenci)) #liste tipi
print(len(ogrenci)) #eleman miktarı
ogrenci.append("Toki") #listeye ekleme sonuna
print(ogrenci)
ogrenci.insert(2,"Hamdi") #sıraya göre ekleme
print(ogrenci)
ogrenci.remove("Hamdi") #silme
print(ogrenci)
ogrenci.pop(2) #2. indextekini silme
print(ogrenci)
print(ogrenci.index(True)) #True nin
ogrenci.reverse() #listeyi
print(ogrenci)

#Tuple
ogrencii=(35,"Merhaba","elma",11,"Armut",True) #Tuple Tarzı liste
print(type(ogrencii)) #liste tipi
print(len(ogrencii)) #eleman miktarı
print("H"*20) #stringi 20 defa yazdırma
print(ogrencii.count(35)) #listede o elemandan kaç tane olduğu
print(ogrencii.index(11)) #listede o elemanın kaçıncı sırada olduğu
ogrencii_list = list(ogrencii) #normal listeye çevirme
print(ogrencii_list) 
ogrencii_list.append("Toki") #liste sonuna eleman ekleme
print(ogrencii_list)
ogrencii= tuple(ogrencii_list) #listeyi tuple li steye çevirme
print(ogrencii)
