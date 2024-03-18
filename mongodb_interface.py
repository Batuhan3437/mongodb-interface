from pymongo import MongoClient
from bson.objectid import ObjectId

# MongoDB bağlantısı
client = MongoClient('"""mongodb connection"""')
db = client['my_veri']
collection = db['veri_seti']

# Verileri MongoDB'den çekin
data = collection.find()
print("Txt dosyasına veri eklemek istiyorsanız 0'a basın\nVeriyi güncellemek istiyorsanız 1'e basın\nVeriyi silmek için 2'ye basın")
veri_text = int(input("\n\nNe yapmak istersiniz:  "))

while True:
    if veri_text == 0:
        # TXT dosyasını oluşturun ve verileri yazın
        with open('veriler.txt', 'w') as txtfile:
            # Verileri TXT dosyasına yazın
            for row in data:
                txtfile.write(str(row) + "\n")
        print("Eklendi")
        break

    elif veri_text == 1:
        Id = input("\n\nGüncellemek istediğiniz verinin id'si nedir: ")
        document_id = ObjectId(Id)
       
        deneyim = int(input("\nKaç yıl deneyiminiz oldu: "))
        suan = int(input("\nŞuan bir yerde çalışıyor musunuz: "))
        farkli = int(input("\nKaç farklı şirkette çalıştınız: "))
        egitim = int(input("\nEğitim Seviyeniz nedir: "))
        uni = int(input("\nEn iyi 10 okuldan mı mezunsunuz: "))
        staj = int(input("\nStajı bizde mi yaptınız: "))
          
        if suan == 1:
            suan = 'evet'
        elif suan == 0:
            suan = 'hayır'
        if egitim == 0:
            egitim = 'Lisans'
        elif egitim == 1:
            egitim = 'Yüksek Lisans'
        elif egitim == 2:
            egitim = 'Master'

        if uni == 1:
            uni = 'evet'
        elif uni == 0:
            uni = 'hayır'

        if staj == 1:
            staj = 'evet'
        elif staj == 0:
            staj = 'hayır'
            
        # Güncel veri
        new_data = {
            'Deneyim (yıl)': deneyim,
            'Suan çalışma durumu': suan,
            'Kaç farklı şirkette çalıştı': farkli,
            'Eğitim Durumu': egitim,
            'En iyi 10 okuldan mezun mu': uni,
            'Stajı girmek istediği şirkette mi yaptı': staj
        }

        # Güncelleme işlemi
        result = collection.update_one({'_id': document_id}, {'$set': new_data})

        # Güncelleme işleminin sonucunu kontrol etme
        if result.modified_count > 0:
            print("\nBelge güncellendi.")
        
        else:
            print("\nGüncelleme yapılmadı.")
        
        print("\n\nEvet için 1 \n Hayır için 0' a basın")
        
        cikis1=int(input("\nTekrar bir islem yapmak istermisiniz: "))
       
        if cikis1==1:
            continue
        
        elif cikis1==0:
            break
        
        else:
             print("\nGeçersiz işlem..")
             break

    elif veri_text == 2:
       
        Id_delete = input("\n\nSilmek istediğiniz verinin id'si nedir: ")
        document_id = ObjectId(Id_delete)
        delete_result = collection.delete_one({'_id': document_id})
        
        print("\nSilinen veri sayısı:", delete_result.deleted_count)
        
        print("\n\nEvet için 1\nHayır için 0' a basın")
        
        cikis=int(input("\nTekrar bir islem yapmak istermisiniz: "))
        
        if cikis==1:
            continue
        
        elif cikis==0:
            break
        
        else:
            print("\nGeçersiz işlem..")
            break
    
    else:
        print("\nGeçersiz işlem..")
        break

client.close()
