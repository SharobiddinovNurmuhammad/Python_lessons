'''
Author: Sharobiddinov Nurmuhammad

Sana: 26.07.2022
'''
#-----------------------
ismlar = ['Javohir', 'Salimjon', "G'anijon"]
print(ismlar)

#-----------------------
print("Salom " + ismlar[0] + " ishlaringiz yaxshimi?")
print(ismlar[1] + " o'qishlaringiz yaxshimi?")
print("Assalomu alaykum " + ismlar[2])

#-----------------------
sonlar = [1, 2, 0, -1, -2, 1_200_345, 19.23, -23.19]
print(sonlar)

#----------------------
sonlar[-2] = 3.14
sonlar[-1] = 2.71
sonlar[-3] = sonlar[-3] + 155
sonlar[0] = sonlar[0] - 1
sonlar[2] = sonlar[2] + 1
print(sonlar)

#----------------------
t_shaxslar = ["Beruniy", 'Nyuton', 'Navoiy', 'Tesla']
z_shaxslar = ["Ilon Mask", 'Stiv Jobs', 'Mark Zuckerberg']

#----------------------
t_shaxs = t_shaxslar.pop(1)
z_shaxs = z_shaxslar.pop(0)
print("Men tarixiy shaxslardan " + t_shaxs + " bilan,\
zamonaviy shaxslardan esa " + z_shaxs + " bilan\
 suhbat qilishni istar edim")
 
#-----------------------
friends = ["Javohir", "Yoqubjon", 'Samandar', 'Xurshid', 'Jasur',"Qobiljon"]
print(friends)

#----------------------
friends.remove('Yoqubjon')
friends.remove("Xurshid")
friends.remove("Jasur")

#----------------------
friends.append("Mashrabjon")
friends.insert(0, 'Elbek')
friends.insert(3,'Umidjon')
print(friends)

#----------------------
mehmonlar = []
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(1))
print(mehmonlar)











