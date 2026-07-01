"""
Python asosiy funksiyalar to'plami
------------------------------------
Ushbu fayl quyidagi mavzular bo'yicha mashq funksiyalarini o'z ichiga oladi:
1. Ism va yosh orqali tug'ilgan yilni hisoblash
2. Sonning kvadrati va kubini hisoblash
3. Son juft yoki toqligini tekshirish
4. Ikki sondan kattasini aniqlash
5. x ning y-darajasini hisoblash (standart qiymat bilan)
6. Sonning 2 dan 10 gacha bo'linishini tekshirish
"""


# 1) Ism va yosh orqali tug'ilgan yilni hisoblash
def ism_yosh(joriy_yil=2026):
    ism = input("Ismingizni kiriting: ")
    yosh = int(input("Yoshingizni kiriting: "))
    t_yil = joriy_yil - yosh
    print(f"Mening ismim {ism}, {t_yil}-yilda tug'ilganman, {yosh} yoshdaman")


# Natija namunasi:
# Ismingizni kiriting: Alisher
# Yoshingizni kiriting: 20
# Mening ismim Alisher, 2006-yilda tug'ilganman, 20 yoshdaman


# 2) Sonning kvadrati va kubini hisoblash
def son_olish():
    son = int(input("Son kiriting: "))
    kvadrat = son ** 2
    kubi = son ** 3
    print(f"{son} ning kvadrati {kvadrat} ga teng, {son} ning kubi esa {kubi} ga teng")


# Natija namunasi:
# Son kiriting: 4
# 4 ning kvadrati 16 ga teng, 4 ning kubi esa 64 ga teng


# 3) Son juft yoki toqligini tekshirish
def juft_toq_tek():
    son = int(input("Son kiriting: "))
    if son % 2 == 0:
        print("Juft son")
    else:
        print("Toq son")


# Natija namunasi:
# Son kiriting: 7
# Toq son


# 4) Ikki sondan kattasini aniqlash
def son_tek():
    son1 = int(input("birinchi sonni kiriting: "))
    son2 = int(input("ikkinchi sonni kiriting: "))
    if son1 > son2:
        print(f"{son1} katta")
    elif son1 < son2:
        print(f"{son2} katta")
    else:
        print("Sonlar teng")


# Natija namunasi:
# birinchi sonni kiriting: 15
# ikkinchi sonni kiriting: 9
# 15 katta


# 5) x ning y-darajasini hisoblash (y uchun standart qiymat 2)
def daraja(x, y=2):
    natija = x ** y
    print(f"{x} ning {y} darajasi {natija} ga teng")


# Natija namunasi:
# x sonni kiriting: 3
# y sonni kiriting: (bo'sh qoldirilsa)
# 3 ning 2 darajasi 9 ga teng


# 6) Sonning 2 dan 10 gacha bo'linishini tekshirish
def qol_tekshir():
    son = int(input("Son kiriting: "))
    for i in range(2, 11):
        if son % i == 0:
            print(f"{son}, {i} larga qoldiqsiz bo'linadi")
        else:
            print(f"{son}, {i} larga qoldiqsiz bo'linmaydi")


# Natija namunasi:
# Son kiriting: 12
# 12, 2 larga qoldiqsiz bo'linadi
# 12, 3 larga qoldiqsiz bo'linadi
# 12, 4 larga qoldiqsiz bo'linadi
# 12, 5 larga qoldiqsiz bo'linmaydi
# 12, 6 larga qoldiqsiz bo'linadi
# 12, 7 larga qoldiqsiz bo'linmaydi
# 12, 8 larga qoldiqsiz bo'linmaydi
# 12, 9 larga qoldiqsiz bo'linmaydi
# 12, 10 larga qoldiqsiz bo'linmaydi



