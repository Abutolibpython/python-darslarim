# -*- coding: utf-8 -*-
"""
Created on Wed May  4 10:34:40 2022
7-dars. LIST(RO'YXAT")
@author: Ucer
"""

#mevalar=["olma", "anjir", "shaftoli", "o'rik"]
#narxlar=[12000, 18000, 10900, 22000]
#sonlar=["bir", "ikki", 3, 4, 5]
#ismlar=[]


#bozorlik=["un", "kartoshka", "piyoz", "sabzi", "go'sht"]
#mahsulot=bozorlik.pop(4)
#print("Men " +mahsulot+" sotib oldim")
#print("Sotib olinmagan mahsulotlar: ", bozorlik)


#Vazifalar

#ismlar=["Abdulaziz", "Akram", "Doniyor"]
#print("Salom " + ismlar[0] + " bugun choyxona bormi?")
#print(ismlar[2], "choyxonaga boramizmi?")

#sonlar=[15, 60, 12.5, -23, 81.6, 115]
#print (sonlar)
#sonlar[0] = sonlar[0]+sonlar[-1]
#sonlar[1] = 70
#sonlar[4] = int(sonlar[4]) + int(19.4)
#del sonlar[2]
#print (sonlar)
 
#t_shaxslar=["Amir Temur", "Imom Buxoriy", "Ibn Sino"]
#z_shaxslar=["Erdug'an", "Bill Gayts", "Zeleniskiy"]
#print("Men tarixiy shaxslardan " + t_shaxslar[1] + " bilan, zamonaviy shaxslardan " + z_shaxslar[0] + " bilan suxbat qilishni istar edim")

friends=[]
friends.append("Abdulaziz")
friends.append("Akram")
friends.append("Olimjon")
friends.append("Doniyor")
friends.append("Oqiljon")
#print(friends)
friends.remove("Olimjon")
friends.remove("Akram")
#print(friends)
friends.append("Abdurahmon")
friends.insert(0, "Alisher")
friends.insert(3, "Abduqodir")
#print(friends)

mexmonlar=[]
mexmonlar.append(friends.pop(3))
mexmonlar.append(friends.pop(0))
mexmonlar.append(friends.pop(-1))
print("\nKelgan mexmonlar: ", mexmonlar)