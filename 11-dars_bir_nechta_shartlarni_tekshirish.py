# -*- coding: utf-8 -*-
"""
Created on Thu May 12 13:50:01 2022
11-dars. Bir necha shartlarni tekshirish
@author: Ucer
"""

#yosh=int(input("Yoshingiz nechida? "))
#if yosh<=4:
#    print("Sizga kirish bepul.")
#elif yosh<=12:
#    print("Sizga kirish 5000 so'm")
#else:
#    print("Sizga kirish 10000 so'm")
    
#yosh=int(input("Yoshingiz nechida? "))
#if yosh<=4:
#    narx=0
#elif yosh<=12:
#    narx=5000
#else:
#    narx=10000
#print(f"Sizga kirish {narx} so'm")

#kun=input("Bugun qaysi kun?>>>") 
#if kun.lower()=="shanba" or kun.lower()=="yakshanba":
#    print("Bugun dam olish kuni.")
#else:
#    print("Bugun ish kuni.")

#kun=input("Bugun kun nima? ")
#harorat=float(input("Havo harorati qanday? "))
#if kun.lower()=="yakshanba" and harorat>=30:
#    print("Cho'milgani ketdik.")
#elif kun.lower()=="yakshanba" and harorat<30:
#    print("Uyda dam olamiz.")

#narx=15000
#choy=True
#salat=False
#if choy and salat:
#    narx=narx + 10000
#elif choy or salat:
#    narx=narx +5000
#print(f"Jami {narx} so'm")

#narx=15000
#choy=True
#salat=False
#non=True
#kompot=False
#assorti=True
#if choy:
#    print("Mijoz choy sotib oldi")
#    narx=narx+3000
#if salat:
#    print("Mijoz salat sotib oldi")
#    narx=narx+5000
#if non:
#    print("Mijoz non sotib oldi")
#    narx=narx+2000
#if kompot:
#    print("Mijoz kompot sotib oldi")
#    narx=narx+6000
#if assorti:
#    print("Mijoz assorti sotib oldi")
#    narx=narx+10000   
#print(f"Jami {narx} so'm") 

#menu=["osh", "qazonkabob", "shashlik", "norin", "somsa"]
#ovqat=input("Nima ovqat buyurasiz? ")
#if ovqat.lower() in menu:
#    print("Buyurtmangiz qabul qilindi!")
#else:
#    print("Afsuski bizda bunday ovqat yo'q.")

#menu=["osh", "qazonkabob", "shashlik", "norin", "somsa"]
#buyurtmalar=["osh", "somsa", "manti", "shashlik"]
#for taom in buyurtmalar:
#    if taom in menu:
#        print(f"Menuda {taom} bor")
#    else:
#        print(f"Kechirasiz menuda {taom} yo'q.")
        

#VAZIFALAR

#1
#son=float(input("Juft son kiriting: "))
#if son%2:
#    print("Bu son juft emas.")
#else:
#    print("Rahmat!")

#2
#yosh=int(input("Yoshingiz nechida? "))
#if yosh<=4 or yosh>60:   
#    narx=0    
#elif yosh<18:
#    narx=10000
#else:
#    narx=20000
#print(f"Chipta narxi {narx} so'm")
    
#3
#x=float(input("Ikkita son kiriting: "))
#y=float(input("Ikkita son kiriting: "))
#if x==y:
#    print(f"{x}={y}")
#elif x>y:
#    print(f"{x}>{y}")
#else:
#    print(f"{x}<{y}")

#4
#mahsulotlar=["go'sht", "kartoshka", "sabzi", "piyoz", "suv", "olma", "semichka", "qulupnay", "pecheniy", "non"]
#savat=[]
#for n in range(5):
#    savat.append(input(f"Savatga {n+1} - mahsulotni qo'shing: "))        
#for mahsulot in savat:
#    if mahsulot in mahsulotlar:
#        print(f"Do'konimizda {mahsulot} bor.")
#    else:
#        print(f"Do'konimizda {mahsulot} yo'q.")

#5
#users=["akram", "abutolib", "abdulaziz", "doniyor", "olimjon"]
#login=input("Yangi login kiriting: ")
#if login in users:
#    print("Login band, yangi login kiriting")
#else:
#    print(f"Xush kelibsiz {login.title()}")

#6
son=int(input("Istalgan butun son kiriting: "))
for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi.")



    