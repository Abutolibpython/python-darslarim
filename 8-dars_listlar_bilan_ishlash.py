# -*- coding: utf-8 -*-
"""
Created on Thu May  5 10:13:26 2022
8-dars. Ro'yhatlar bilan ishlash'
@author: Ucer
"""

cars=["BMW", "Mersedes", "Volvo", "General Motors", "Tesla", "Audi"]
#print(cars)
#cars.sort()
#print(cars)
#cars.sort(reverse = True)
#print(sorted(cars))
#print(sorted(cars, reverse=True))

sonlar=[15, 55, -13, 2.3, -9.1, 50]
#sonlar.sort()
#sonlar.sort(reverse = True)
#print(sonlar)

#cars.reverse()
#print (cars)

sonlar=list(range(0,10))
#print(sonlar)

#toq_sonlar= list(range(1,20,2))
#print(toq_sonlar)
#juft_sonlar=list(range(0,20,2))
#print(juft_sonlar)

narxlar=[12000, 22500, 23456, 9800, 5600, 9934, 32870]
arzon=min(narxlar)
qimmat=max(narxlar)
jami=sum(narxlar)
#print("Eng arzon narx - ", arzon, " eng qimmat narx - ", qimmat, " jami: ", jami)

#print(cars[0:4])


my_cars=cars[:]
#print(my_cars)
my_cars.remove("Volvo")
#print(my_cars)
my_cars[0]="Lacetti"
#print(my_cars)
my_cars.append("BMW")
#print(my_cars)
my_cars.insert(0,"Gentra")
#print(my_cars)

toys=("bus", "car", "bear", "dina", "lizard")
#print(toys)
#toys.append("teddy")
#print(toys)
toys=list(toys)
toys.append("teddy")
#print (toys)
toys=tuple(toys)
#print (toys)


#Vazifalar

davlatlar=["O'zbekiston", "Xitoy", "AQSH", "Angliya", "Ispaniya"]
#print(davlatlar)

#print(sorted(davlatlar))
#print(sorted(davlatlar, reverse=True))
#print(davlatlar)
#davlatlar.reverse()
#print(davlatlar)
#davlatlar.sort()
#print(davlatlar)
#davlatlar.sort(reverse=True)
#print(davlatlar)

juft_sonlar=list(range(200,1200,2))
#print(juft_sonlar)
#jami=sum(juft_sonlar)
#print(jami)

kichik=min(juft_sonlar)
katta=max(juft_sonlar)
#print("Ushbu juft sonlarning eng katta va eng kichik sonlarining ayirmasi: ", katta-kichik, " ga teng")

#print(juft_sonlar[:20])
#print(juft_sonlar[-20:])

taomlar=["osh", "shashlik", "shurva", "mastava", "kabob"]
#print(taomlar)
nonushta=taomlar[:]
#print(nonushta)
nonushta.remove("shashlik")
nonushta.remove("kabob")
nonushta.append("qaymoq")
nonushta.append("non")
#print(nonushta)

#print(taomlar)
#print(nonushta)

nonushta=tuple(nonushta)
nonushta[0]="tuxum"
print(nonushta)


































