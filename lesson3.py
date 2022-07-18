"""
Author: Sharobiddinov Nurmuhammad

Sana: 18.07.2022
"""
#Pythonda quydagi o'zgaruvchilarni yarating:
kocha = "Bog'bon"
mahalla = "Sag'bon"
tuman = "Bodomzor"
viloyat = "Samarqand"

#Yuqoridagi o'zgaruvchilarni jamlab, quydagi ko'rinishda konsolga chiqaring: Bog'bon ko'chasi, Sag'bon mahallasi, Bodomzor tumani, Samarqand viloyat
print(kocha + " ko'chasi, " + mahalla +  " mahallasi, " + tuman + " tumani, " + viloyat + " viloyati")

#Yuqoridagi o'zgaruvchilarni qiymatini foydalanuvchidan so'rang.Va avvalgi mashqni takrorlang.
kocha = input("Ko'cha nomi: ")
mahalla = input("Mahalla nomi: ")
tuman = input("Tuman nomi: ")
viloyat = input("Viloyat nomi: ")
print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")

#Yuqoridagi matnni konsolga chiqaring konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing.
print(f"{kocha} ko'chasi,\n{mahalla} mahallasi,\n{tuman} tumani,\n{viloyat} viloyati")

#Yuqoridagi matnni f-string yordamida yangi, manzil deb nomlangan o'zgaruvchiga yuklang.
manzil = f"{kocha} ko'chasi,\n{mahalla} mahallasi,\n{tuman} tumani,\n{viloyat} viloyati"

#manzil o'zgaruvchisiga biz yuqorida o'rgangan title(),upper(),lower(),capitalize() metodlari qo'llab ko'ring
print(manzil.upper())
print(manzil.lower())
print(manzil.title())
print(manzil.capitalize())