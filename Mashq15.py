# ============================================================
# TOPSHIRIQ 1
# Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing.
# Lug'atdagi har bir kalit va qiymatni for tsikli yordamida,
# alifbo ketma-ketligida chiroyli qilib konsolga chiqaring.
# ============================================================

lugatlar = {"integer": "butun son",
            "string": "matn",
            "float": "kasr son",
            "boolean": "mantiqiy qiymat",
            "complex": "murakkab son",
            "if": "agar",
            "else": "aks holda",
            "for": "uchun",
            "loop": "sikl",
            "def": "funksiya"}

for atama in sorted(lugatlar):
    print(atama, " - ", lugatlar[atama])

# Natija:
# boolean  -  mantiqiy qiymat
# complex  -  murakkab son
# def  -  funksiya
# else  -  aks holda
# float  -  kasr son
# for  -  uchun
# if  -  agar
# integer  -  butun son
# loop  -  sikl
# string  -  matn


# ============================================================
# TOPSHIRIQ 2
# Davlatlar va ularning poytaxtlari lug'atini tuzing.
# Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida,
# alifbo ketma-ketligida konsolga chiqaring.
# ============================================================

davlatlar_poytaxt = {"Ozbekiston": "Toshkent",
                      "Rossiya": "Moskva",
                      "Fransiya": "Parij",
                      "Xitoy": "Pekin",
                      "Turkiya": "Anqara",
                      "Angliya": "London",
                      "Germaniya": "Berlin",
                      "AQSH": "Vashington",
                      "Italiya": "Rim",
                      "Yaponiya": "Tokio"}

for davlat in sorted(davlatlar_poytaxt.keys()):
    print(davlat)

for poytaxt in sorted(davlatlar_poytaxt.values()):
    print(poytaxt)

# Natija:
# AQSH
# Angliya
# Fransiya
# Germaniya
# Italiya
# Ozbekiston
# Rossiya
# Turkiya
# Xitoy
# Yaponiya
#
# Anqara
# Berlin
# London
# Moskva
# Parij
# Pekin
# Rim
# Toshkent
# Vashington
# Tokio


# ============================================================
# TOPSHIRIQ 3
# Foydalanuvchidan istalgan davlatni kiritishni so'rang va
# shu davlatning poytaxtini konsolga chiqaring.
# Agar foydalanuvchi lug'atda yo'q davlatni kiritsa,
# "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.
# ============================================================

davlatlar_poytaxt = {"Ozbekiston": "Toshkent",
                      "Rossiya": "Moskva",
                      "Fransiya": "Parij",
                      "Xitoy": "Pekin",
                      "Turkiya": "Anqara",
                      "Angliya": "London",
                      "Germaniya": "Berlin",
                      "AQSH": "Vashington",
                      "Italiya": "Rim",
                      "Yaponiya": "Tokio"}

davlat = input("Davlatni kiriting: ")
if davlat in davlatlar_poytaxt:
    print(f"Bu davlatning poytaxti {davlatlar_poytaxt[davlat]}")
else:
    print("Bizda bunday malumot yoq")

# Natija (misol 1):
# Davlatni kiriting: Fransiya
# Bu davlatning poytaxti Parij
#
# Natija (misol 2):
# Davlatni kiriting: Braziliya
# Bizda bunday malumot yoq


# ============================================================
# TOPSHIRIQ 4
# Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting).
# Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang.
# Foydalanuvchi kiritgan taomlarni menu bilan solishtiring,
# agar taom menuda bo'lsa narhini ko'rsating,
# aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.
# ============================================================

menu = {"Osh": 30000,
        "Manti": 25000,
        "Somsa": 10000,
        "Shorva": 25000,
        "Shashlik": 12000,
        "Baliq": 45000,
        "Chuchvara": 30000,
        "Olivia": 20000,
        "Sezir": 20000,
        "Burger": 20000}

for x in range(3):
    buyurtma = input("buyurtma bering: ")
    if buyurtma in menu:
        print(f"bu taomning narxi: {menu[buyurtma]}")
    else:
        print("bu taom bizda yoq")

# Natija (misol):
# buyurtma bering: Osh
# bu taomning narxi: 30000
# buyurtma bering: Pitsa
# bu taom bizda yoq
# buyurtma bering: Burger
# bu taomning narxi: 20000
