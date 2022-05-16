# -*- coding: utf-8 -*-
"""
Created on Fri May  6 16:43:06 2022
9-dars. For takrorlash operatori
@author: Ucer
"""

#mehmonlar=["Ali", "Vali", "Hasan", "Husan", "Olim"]
#print("Salom ", mehmonlar[0])
#print("Salom ", mehmonlar[1])
#for mehmon in mehmonlar:
#     print("Hurmatli ", mehmon, "sizni 28 may kuni futbol oqshomiga taklif etamiz")
#     print("Hurmat bilan, 9 'A' sinfdoshlar\n")
     
#sonlar=list(range(1,11))
#for son in sonlar:
#    print(f"{son} ning kvadrati {son**2} ga teng\n")     
 
#sonlar=list(range(11)) 
#sonlar_kvadrati=[]
#for son in sonlar:
#    sonlar_kvadrati.append(son**2)
#print(sonlar)
#print(sonlar_kvadrati)


#dostlar=[]
#print("5 ta eng yaqin do'stingiz kim?")
#for n in range(5):
#    dostlar.append(input(f"{n+1} - do'stingizni ismini kiriting: "))
#print(dostlar)
 

#Vazzifalar

#ismlar=["Akram","Abdulaziz", "Doniyor", "Olimjon", "Mansur"]
#for ism in ismlar:
#    print("Salom ", ism)
#print(f"Kod {len(ismlar)} marta takrorlandi")

#toq_sonlar=list(range(11,100,2))
#for son in toq_sonlar:
#    print(son**3)

#kinolar=[]
#print("Eng sevimli kinolaringizni kiriting: ")
#for k in range(5):
#    kinolar.append(input(f"{k+1} - kinoni kiriting: ")) 
#print(kinolar)

n_people=int(input("Bugun necha kishi bilan suhbat qurdingiz?>>>"))
ismlar=[]
for n in range(n_people):
    ismlar.append(input(f"{n+1} - suhbat qurgan odamingiz kim edi: "))
print(ismlar)    