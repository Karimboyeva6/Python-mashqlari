# =========================================================
# 1-misol: "gm" bo'lsa katta harf, qolganlari Title Case bo'lib chiqadi
# =========================================================
cars = ["toyota", "mazda", "hyundai", "gm", "kia"]

for car in cars:
    if car == "gm":
        print(car.upper())   # gm -> GM
    else:
        print(car.title())   # toyota -> Toyota va h.k.

# Natija:
# Toyota
# Mazda
# Hyundai
# GM
# Kia


# =========================================================
# 2-misol: yuqoridagi bilan bir xil mantiq, shart teskari yozilgan (natija bir xil)
# =========================================================
cars = ["toyota", "mazda", "hyundai", "gm", "kia"]

for car in cars:
    if car != "gm":
        print(car.title())
    else:
        print(car.upper())

# Natija (1-misol bilan bir xil):
# Toyota
# Mazda
# Hyundai
# GM
# Kia


# =========================================================
# 3-misol: login "admin" bo'lsa maxsus xabar, aks holda oddiy salomlashish
# =========================================================
login = input("Login kiriting: ")

if login == "admin":
    print("Xush kelibsiz, Admin. Foydalanuvchilar roʻyxatini koʻrasizmi?")
else:
    print(f"Xush kelibsiz, {login}!")

# Masalan: login = "admin" -> "Xush kelibsiz, Admin. Foydalanuvchilar roʻyxatini koʻrasizmi?"
# login = "ali"   -> "Xush kelibsiz, ali!"


# =========================================================
# 4-misol: ikki sonni solishtirish (teng yoki teng emasligini tekshiradi)
# =========================================================
son1 = int(input('Birinchi sonni kiriting?: '))
son2 = int(input("Ikkinchi sonni kiriting?: "))

if son1 == son2:
    print("ikkala son teng")
else:
    print("ikkala son teng emas")

# Masalan: son1=5, son2=5 -> "ikkala son teng"
# son1=5, son2=7 -> "ikkala son teng emas"


# =========================================================
# 5-misol: kiritilgan sonning musbat yoki manfiyligini aniqlaydi
# =========================================================
son = int(input("istalgan son kiriting?: "))

if son > 0:
    print('musbat son')
else:
    print("manfiy son")

# Eslatma: son = 0 bo'lsa ham "manfiy son" deb chiqadi,
# chunki shart faqat (son > 0) ni tekshiradi, 0 va manfiy sonlar bir xil
# shoxobchaga (else) tushib qoladi - bu mantiqiy xato hisoblanadi.
# Masalan: son=10 -> "musbat son"
#          son=-3 -> "manfiy son"
#          son=0  -> "manfiy son" (noto'g'ri, lekin kod shunday ishlaydi)


# =========================================================
# 6-misol: musbat sonning kvadrat ildizini hisoblaydi
# =========================================================
son = float(input("Son kiriting: "))

if son > 0:
    ildiz = son ** 0.5
    print(f"Ildizi: {ildiz}")
else:
    print("Musbat son kiriting:")

# Masalan: son=16 -> "Ildizi: 4.0"
# son=-4 -> "Musbat son kiriting:" (manfiy sonlardan oddiy ildiz olinmaydi)
