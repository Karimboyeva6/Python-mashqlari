# ==========================================================
# MASHQ 1
# Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur
# shaxslar haqidagi ma'lumotlarni lug'at ko'rinishida saqlang.
# Lug'atlarni bitta ro'yxatga joylang va har bir shaxs haqidagi
# ma'lumotni konsolga chiqaring.
# ==========================================================

shaxs1 = {'Ismi': 'Alisher Navoiy',
          'Sohasi': 'yozuvchi'}
shaxs2 = {'Ismi': 'Bobur',
          'Sohasi': 'Shoh va shoir'}
shaxs3 = {'Ismi': 'Imom Buxoriy',
          'Sohasi': 'Hadisshunos'}
shaxs4 = {'Ismi': 'Amir Temur',
          'Sohasi': 'Sohibqiron sarkarda'}

shaxslar = [shaxs1, shaxs2, shaxs3, shaxs4]

for shaxs in shaxslar:
    print(shaxs)

# NATIJA:
# {'Ismi': 'Alisher Navoiy', 'Sohasi': 'yozuvchi'}
# {'Ismi': 'Bobur', 'Sohasi': 'Shoh va shoir'}
# {'Ismi': 'Imom Buxoriy', 'Sohasi': 'Hadisshunos'}
# {'Ismi': 'Amir Temur', 'Sohasi': 'Sohibqiron sarkarda'}


# ==========================================================
# MASHQ 2
# Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari
# ro'yxatini ham qo'shing. For tsikli yordamida muallifning
# ismi va uning asarlarini konsolga chiqaring.
# ==========================================================

shaxs1 = {'Ismi': 'Alisher Navoiy',
          'Sohasi': 'yozuvchi',
          'Asarlari': ['Xamsa', 'Lison ut-Tayr', 'Mahbub ul-Qulub']}
shaxs2 = {'Ismi': 'Bobur',
          'Sohasi': 'Shoh va shoir',
          'Asarlari': ['Boburnoma', 'Devon', 'Mubayyan']}
shaxs3 = {'Ismi': 'Imom Buxoriy',
          'Sohasi': 'Hadisshunos',
          'Asarlari': ['Sahih al Buxoriy', 'At-tarix al-Kabir']}
shaxs4 = {'Ismi': 'Amir Temur',
          'Sohasi': 'Sohibqiron sarkarda',
          'Asarlari': ['Temur tuzuklari']}

shaxslar = [shaxs1, shaxs2, shaxs3, shaxs4]

for shaxs in shaxslar:
    print(f"Ism: {shaxs['Ismi']}")
    print(f"Asari: {shaxs['Asarlari']}")

# NATIJA:
# Ism: Alisher Navoiy
# Asari: ['Xamsa', 'Lison ut-Tayr', 'Mahbub ul-Qulub']
# Ism: Bobur
# Asari: ['Boburnoma', 'Devon', 'Mubayyan']
# Ism: Imom Buxoriy
# Asari: ['Sahih al Buxoriy', 'At-tarix al-Kabir']
# Ism: Amir Temur
# Asari: ['Temur tuzuklari']


# ==========================================================
# MASHQ 3
# Oila a'zolaringiz (do'stlaringiz)dan 3 ta sevimli kino-serial
# haqida so'rang. Do'stingiz ismi kalit, uning sevimli kinolari
# esa ro'yxat ko'rinishida lug'atga saqlang. Natijani konsolga
# chiqaring.
# ==========================================================

sevimli_kino = {'Qunduz': ['Qatiyat', 'Interstellar', 'Yashil kitob'],
                'Gavhar': ['Suyunchi', 'Mahallada duv duv gap', 'Oyna oyna'],
                'Yulduz': ['Matritsa', 'Vatan', 'Novda']}

for ism, kinolar in sevimli_kino.items():
    print(f"{ism}ning sevimli kinosi: {kinolar}")

# NATIJA:
# Qunduzning sevimli kinosi: ['Qatiyat', 'Interstellar', 'Yashil kitob']
# Gavharning sevimli kinosi: ['Suyunchi', 'Mahallada duv duv gap', 'Oyna oyna']
# Yulduzning sevimli kinosi: ['Matritsa', 'Vatan', 'Novda']


# ==========================================================
# MASHQ 4
# "Davlatlar" degan lug'at yarating. Lug'at ichida bir nechta
# davlatlar haqida ma'lumotlarni lug'at ko'rinishida saqlang.
# Har bir davlat haqida ma'lumotni konsolga chiqaring.
# ==========================================================

davlatlar = {"Ozbekiston": {"poytaxt": "Toshkent", "aholisi": "36 mln"},
             "Fransiya": {"poytaxt": "Parij", "aholisi": "67 mln"},
             "Yaponiya": {"poytaxt": "Tokio", "aholisi": "125 mln"}}

for nomi, malumot in davlatlar.items():
    print(f"{nomi}ning aholisi {malumot['aholisi']}ga teng")

# NATIJA:
# Ozbekistonning aholisi 36 mlnga teng
# Fransiyaning aholisi 67 mlnga teng
# Yaponiyaning aholisi 125 mlnga teng


# ==========================================================
# MASHQ 5
# Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha
# davlatlarni emas, foydalanuvchi so'ragan davlat haqida
# ma'lumot bering. Agar davlat lug'atda mavjud bo'lmasa,
# "Bizda bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring.
# ==========================================================

davlatlar = {"Ozbekiston": {"poytaxt": "Toshkent", "aholisi": "36 mln"},
             "Fransiya": {"poytaxt": "Parij", "aholisi": "67 mln"},
             "Yaponiya": {"poytaxt": "Tokio", "aholisi": "125 mln"}}

davlat_nomi = input("Davlatni kiriting: ")

if davlat_nomi in davlatlar:
    malumot = davlatlar[davlat_nomi]
    print(f"{davlat_nomi}: poytaxti - {malumot['poytaxt']}, aholisi - {malumot['aholisi']}")
else:
    print("Bizda bu davlat haqida ma'lumot yo'q")

# NATIJA (masalan "Fransiya" kiritilsa):
# Davlatni kiriting: Fransiya
# Fransiya: poytaxti - Parij, aholisi - 67 mln
#
# NATIJA (masalan "Germaniya" kiritilsa, lug'atda yo'q):
# Davlatni kiriting: Germaniya
# Bizda bu davlat haqida ma'lumot yo'q
