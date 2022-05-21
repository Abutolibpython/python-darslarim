# -*- coding: utf-8 -*-
"""
Created on Wed May 18 16:29:43 2022
16-dars.Nesting
@author: Ucer
"""
car0={"model":"lacetti",
      "rang":"oq",
      "yil":2018,
      "narx":13000,
      "km":50000,
      "karobka":"avtomat"
      }

car1={"model":"nexia 3",
      "rang":"qora",
      "yil":2015,
      "narx":9000,
      "km":89000,
      "karobka":"mehanika"
      }

car2={"model":"gentra",
      "rang":"qizil",
      "yil":2019,
      "narx":15000,
      "km":20000,
      "karobka":"mehanika"
      }

#car=car0
#print(f"{car['model'].title()}, "
 #     f"{car['rang']} rang, "
 #     f"{car['yil']}-yil, {car['narx']}$")

#car=car1
#print(f"{car['model'].title()}, "
#      f"{car['rang']} rang, "
#      f"{car['yil']}-yil, {car['narx']}$")

#cars=[car0, car1, car2]
#for car in cars:
#    print(f"{car['model'].title()}, "
 #     f"{car['rang']} rang, "
 #     f"{car['yil']}-yil, {car['narx']}$")

#print(cars[0]["model"])

#print(f"{cars[2]['rang'].title()} {cars[2]['model']}")

#malibus=[]
#for n in range(10):
#    new_car={"model":"malibu",
#             "rang":None,
#             "yil":2022,
#             "narx":None,
#             "km":0,
#             "karobka":"avtomat"
#             }
#    malibus.append(new_car)
#for malibu in malibus:
#    print(malibu)

#for malibu in malibus[:3]:
#    malibu["rang"]="oq"
#for malibu in malibus[3:6]:
#    malibu["rang"]="qora"
#for malibu in malibus[6:]:
#    malibu["rang"]="qora"
#    malibu ["karobka"]="mehanika"

#for malibu in malibus:
#    print(malibu)

#for malibu in malibus:
#    if malibu["karobka"]=="avtomat":
#        malibu["narx"]=40000
#    else:
#        malibu["narx"]=35000
#for malibu in malibus:
#    print(malibu)
 
#dasturchilar={
#    "ali":["python", "c++"],
#    "vali":["html", "css", "js"],
#    "hasan":["php", "sql"],
#    "husan":["python", "php"],
#    "maryam":["c++", "c#"]
#    }
#for ism, tillar in dasturchilar.items():
#    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
#    for til in tillar:
#        print(til.upper())

#for ism, tillar in dasturchilar.items():
#    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
#    for til in tillar:
#        print(f"{til.upper()} ", end=" ")

#hamkasblar={
#    "ali":{"familiya":"valiyev",
#          "t_yil":1995,
#          "malumot":"oliy",
#          "tillar":["python", "c++"]},
#    "vali":{"familiya":"aliyev",
#          "t_yil":2001,
#          "malumot":"o'rta mahsus",
#          "tillar":["html", "css", "js"]},
#    "hasan":{"familiya":"husanov",
#          "t_yil":1999,
#          "malumot":"mahsus",
#          "tillar":["python", "php"]},
#    }
#for ism, info in hamkasblar.items():
#    print(f"\n{ism.title()} {info['familiya'].title()}, " 
#          f"{info['t_yil]'}-yilda tug'ilgan."
#          f"Ma'lumoti: {info['malumot']}.\n"
#          "Quyidagi dasturlash tillarini biladi:")
#    for til in info['tillar']:
#        print(til.upper())
        
    
#Vazifalar

#1
#buxoriy={"ism":"ismoil buhoriy",
#         "t_yil":810,
#         "v_yil":870,
#         "t_joy":"buxoro"}
#qodiriy={"ism":"abdulla qodiriy",
#         "t_yil":1894,
#         "v_yil":1938,
#         "t_joy":"toshkent"}
#vohidov={"ism":"erlin vohidov",
#         "t_yil":1936,
#         "v_yil":2016,
#         "t_joy":"farg'ona"}
#navoiy={"ism":"alisher navoiy",
#         "t_yil":1441,
#         "v_yil":1501,
#         "t_joy":"xirot"}
#shaxslar=[buxoriy, qodiriy, vohidov, navoiy]
#for shaxs in shaxslar:
#    ism=shaxs["ism"]
#    t_yil=shaxs["t_yil"]
#    v_yil=shaxs["v_yil"]
#    t_joy=shaxs["t_joy"]
#    print(f"{ism.title()} {t_yil}-yilda {t_joy.title()} shahrida tavallud topgan. "
#          f"{v_yil-t_yil} yil umr ko'rgan")

#2
#shaxslar={
#    "Ismoil Buxoriy":["Al-jome as-saxix", "Al-adab al-mufrad", "At-tarix al-kabir", "At-tarix as-sag'ir"],
#    "Abdulla Qodiriy":["O'tkan kunlar", "Mehrobdan chayon", "Obid ketmon"],
#    "Erkin Vohidov":["Tong nafasi", "Qo'shiqlarim sizga", "O'zbegim", "Qiziquvchan Matmusa"],
#    "Alisher Navoiy":["Xamsa", "Lison ut-tayr", "Mahbub ul-qulub", "Munojot"]
#    }
#for ism, asarlar in shaxslar.items():
#    print(f"{ism.title()}ning mashhur asarlari:")
 #   for asar in asarlar:
#        print(asar)

#3
#kinolar={"ali":["Terminator", "Rambo", "Titanic"],
#         "vali":["Tenet", "Inception", "Intersteller"],
#         "xasan":["Abdullajon", "Bomba", "Shaytanat"],
#         "xusan":["Mahallada duv-duv gap", "John Wick"]
#         }
#for ism, kinolar in kinolar.items():
#    print(f"\n {ism.title()}ning sevimli kinolari:")
#    for kino in kinolar:
#        print(kino)

#4
davlatlar={
    "O'zbekiston":{"poytaxt":"Toshkent",
                   "maydon":448978,
                   "aholi":33_000_000,
                   "pul birligi":"so'm"},
    "Rossiya":{"poytaxt":"Moskva",
                   "maydon":17098246,
                   "aholi":144_000_000,
                   "pul birligi":"rubl"},
    "Aqsh":{"poytaxt":"Vashington",
                   "maydon":9631418,
                   "aholi":327_000_000,
                   "pul birligi":"dollar"},
    "Malayziya":{"poytaxt":"Kuala-Lumpur",
                   "maydon":329750,
                   "aholi":25_000_000,
                   "pul birligi":"rinngit"}
          }
#for davlat, info in davlatlar.items():
#    print(f"\n{davlat.title()}ning poytaxti {info['poytaxt'].title()}\n"
#          f"Hududi: {info['maydon']}\n"
#          f"Aholisi: {info['aholi']}\n"
#          f"Pul birligi: {info['pul birligi']}")

#5
davlatlar={
    "O'zbekiston":{"poytaxt":"Toshkent",
                   "maydon":448978,
                   "aholi":33_000_000,
                   "pul birligi":"so'm"},
    "Rossiya":{"poytaxt":"Moskva",
                   "maydon":17098246,
                   "aholi":144_000_000,
                   "pul birligi":"rubl"},
    "Aqsh":{"poytaxt":"Vashington",
                   "maydon":9631418,
                   "aholi":327_000_000,
                   "pul birligi":"dollar"},
    "Malayziya":{"poytaxt":"Kuala-Lumpur",
                   "maydon":329750,
                   "aholi":25_000_000,
                   "pul birligi":"rinngit"}
        }
davlat=input("Davlat nomini kiriting: ")
if davlat in davlatlar:
    info=davlatlar[davlat]
    print(f"\n{davlat.title()}ning poytaxti {info['poytaxt'].title()}\n"
          f"Hududi: {info['maydon']} kv.km\n"
          f"Aholisi: {info['aholi']}\n"
          f"Pul birligi: {info['pul birligi']}")
else:
    print("Bizda bu davlat haqida ma'lumot mavjud emas")
    






























            
             
             
             
             
             