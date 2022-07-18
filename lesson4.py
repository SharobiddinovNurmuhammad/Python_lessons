"""
Author: Sharobiddov Nurmuhammad

Sana: 18.07.2022
"""
#Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur
son = int(input("Son kiriting: "))
print(son, "ning kvadrati", son**2, "ga teng")
print(son, "ning kubi", son**3, "ga teng")

#Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab, konsolga chiqaruvchi dastur.
yosh = int(input("Yoshingizni kiriting: "))
t_yil = 2022 - yosh
print("Sizning tug'ulgan yilingiz:",t_yil)

#Foydalanuvchidan ikki son kiritishni so'rab, kiritilgan sonlarning yig'indisi, ayirmasi, ko'paytmasi va bo'linmasini chiqaruvchi dastur
son1 = float(input("1-sonni kiriting: "))
son2 = float(input("2-sonni kiriting: "))
print(f"{son1} + {son2} = {son1 + son2}")
print(f"{son1} - {son2} = {son1 - son2}")
print(f"{son1} * {son2} = {son1 * son2}")
print(f"{son1} / {son2} = {son1 / son2}")