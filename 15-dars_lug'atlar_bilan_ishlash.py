# -*- coding: utf-8 -*-
"""
Created on Tue May 17 16:24:46 2022
15-dars. Lug'atlar bilan ishlash.
@author: Ucer
"""

talaba_0={"ism":"alijon",
          "familiya":"shamsiyev",
          "yosh":22,
          "fakultet":"matematika",
          "kurs":4
          }
#print(talaba_0["ism"])

#print(talaba_0.items())

#for kalit, qiymat in talaba_0.items():
#    print(f"Kalit: {kalit}")
#    print(f"Qiymat: {qiymat}")
    
telefonlar={
    "ali":"iphone 13",
    "vali":"galaxy s9",
    "olim":"mi 10",
    "orif":"nokia 3310"
    }
#for k, q in telefonlar.items():
#    print(f"{k.title()}ning telefoni {q}")
    
mahsulotlar={
    "olma":10000,
    "anor":20000,
    "uzum":40000,
    "anjir":25000,
    "shaftoli":30000,
    }
#print(mahsulotlar.keys())

#print("Do'kondagi mahsulotlar: ")
#for mahsulot in mahsulotlar.keys():
#    print(mahsulot.title())

#bozorlik=["anor", "uzum", "non", "baliq"]
#for mahsulot in mahsulotlar:
#    if mahsulot in bozorlik:
#        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")

#for buyum in bozorlik:
#    if not buyum in mahsulotlar:
#        print(f"Iltimos do'koningizga {buyum} ham olib keling.")

#print("Do'konimizdagi mahsulotlar: ")
#for mahsulot in sorted(mahsulotlar):
#    print(mahsulot.title())
    
#print(telefonlar.values())
 
#print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi: ")
#for tel in telefonlar.values():
#    print(tel.title())   
telefonlar={
    "ali":"iphone 13",
    "vali":"galaxy s9",
    "olim":"mi 10",
    "orif":"nokia 3310",
    "hamida":"galaxy s9",
    "maryam":"huawei p30",
    "tohir":"iphone 13",
    "umar":"iphone 13"}
#print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi: ")
#for tel in telefonlar.values():
#    print(tel.title())      
 
#print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi: ")
#for tel in set(telefonlar.values()):
#    print(tel.title())      
    
#toys={"ball", "car", "lamp", "ball"}
#print(toys)
 
    
#Vazifalar

#python_izohli_lugati={"integer":"butun son",
#                     "float":"o'nlik son",
#                      "string": "matn",
#                      "list":"ro'yhat",
#                      "tuple":"o'zgarmas ro'yhat",
#                     "boolean":"mantiqiy qiymat",
#                      "for":"biror amalni qayta bajarish tsikli",
#                     "if":"shartlarni tekshirish operatori"
 #                     }
#for key, value in python_izohli_lugati.items():
#    print(f"{key.title()} - {value}")

#davlatlar={"o'zbekiston":"toshkent",
 #          "aqsh":"washington",
 #          "rossiya":"moskva",
 #          "tojikiston":"dushanbe",
  #         "qirg'iziston":"bishkek",
   #        "qozog'iston":"nursulton",
    #       "malayziya":"kuala-lumpur",
     #      "angliya":"london",
     #      "turkiya":"anqara"
      #     }
#print("Dunyo davlatlari: ")
#for davlat in sorted(davlatlar.keys()):
#    print(davlat.upper())
    
#print("Dunyo davlatlari poytaxtlari:")
#for poytaxt in sorted(davlatlar.values()):
#    print(poytaxt.title())    
 
#country=input("Qaysi davlatni poytaxtini bilishni istaysiz? ").lower()
#capital=davlatlar.get(country)
#if capital==None:
#    print("Kechirasiz bizda bu haqida ma'lumot yo'q")
#else:
#    print(f"{country.title()} davlatining poytaxti {capital.title()} shahri")
    
menu={"osh":15000,
      "shashlik":10000,
      "manti":6000,
      "shurva":13000,
      "somsa":5000,
      "qotirma":20000
      }
print("3 ta taom buyurtma qiling:")
buyurtmalar=[]
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom: ").lower())
                       
for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
    else:
        print(f"Kechirasiz bizda {buyurtma} yo'q")                        
    
 
    
 
    
 