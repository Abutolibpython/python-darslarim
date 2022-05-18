# -*- coding: utf-8 -*-
"""
Created on Mon May 16 14:07:33 2022
14-dars. Dictionary(Lug'at)
@author: Ucer
"""
#car_0={"model" : "ferrari", "rang" : "qizil"}
#print(car_0["model"])
#print(car_0["rang"])

#eng_uzb={"apple":"olma", "apricot":"o'rik", "banana":"banan"}
#print(eng_uzb["apple"]) 

#mevalar={"olma":10000, "tarvuz":15000, "qovun":20000}
#print(f"Olma narhi {mevalar['olma']} so'm")

#talaba_0={"ism":"abutolib qodirov", "yosh":31, "t_yil":1991}
#print(f"{talaba_0['ism'].title()}, {talaba_0['t_yil']}-yilda tug'ilgan, {talaba_0['yosh']} yoshda")
#talaba_0["kurs"]=4
#talaba_0["fakultet"]="iqtisodiyot"
#talaba_0["ism"]="abdulloh"
#print(talaba_0)

#talaba_1={}
#talaba_1["ism"]="abdulloh"
#talaba_1["kurs"]=3
#talaba_1["yosh"]=20
#print(talaba_1)
#print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kursda")
#talaba_1["kurs"]=4
#print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kursda")

#del talaba_0["yosh"]
#print(talaba_0)

#telefonlar={
#    "ali":"iphone 13",
#    "vali":"galaxy s9",
#    "olim":"mi 10",
#    "orif":"nokia 3310"
#    }
#print(telefonlar)


#Vazifalar

#1
#otam={"ism":"ahadjon", "t_yil":1953, "viloyat":"namangan"}
#print(f"Mening otamning ismlari {otam['ism'].title()}. Ular {otam['t_yil']}-yilda {otam['viloyat'].title()} viloyatida tug'ilganlar.")

#2
#taomlar={
#    "otam":"osh",
#    "onam":"mastava",
#    "akam":"shurva",
#    "opam":"makaron",
#    "men":"manti"
#    }
#print(f"Otam {taomlar['otam']}, onam {taomlar['onam']}, akam esa {taomlar['akam']} taomlarini yoqtirishadi.")

#3
python_izohli_lugati={"integer":"butun son",
                      "float":"o'nlik son",
                      "string": "matn",
                      "list":"ro'yhat",
                      "tuple":"o'zgarmas ro'yhat"}
#print(python_izohli_lugati["string"])

#kalit=input("Kalit so'z kiring: ")
#print(python_izohli_lugati.get(kalit, "Bunday so'z mavjud emas."))

kalit=input("Kalit so'z kiring: ")
tarjima=python_izohli_lugati.get(kalit)
if tarjima==None:
    print("Bunday so'z mavjud emas.")
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi.")
























