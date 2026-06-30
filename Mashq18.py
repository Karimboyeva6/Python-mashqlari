# ============================================
# 1-MASHQ: Buyurtma qabul qilish dasturi
# Foydalanuvchidan mahsulot nomlarini birma-bir
# qabul qilib, ro'yxatga joylaydi
# ============================================

buyurtmalar = []
while True:
    buyurtma = input("nma buyurtma berasiz?")
    if buyurtma.lower() == "stop":
        break
    buyurtmalar.append(buyurtma)

print(buyurtmalar)

# Natija (misol):
# nma buyurtma berasiz? olma
# nma buyurtma berasiz? sut
# nma buyurtma berasiz? stop
# ['olma', 'sut']


# ============================================
# 2-MASHQ: E-bozor lug'atini shakllantirish
# Mahsulot nomi va narxini lug'atga joylaydi
# ============================================

e_bozor = {}
while True:
    nomi = input("Mahsulot nomini kiriting:")
    if nomi == "stop":
        break
    else:
        narx = int(input(f"{nomi} narxi"))
        e_bozor[nomi] = narx

print(e_bozor)

# Natija (misol):
# Mahsulot nomini kiriting: olma
# olma narxi5000
# Mahsulot nomini kiriting: non
# non narxi3000
# Mahsulot nomini kiriting: stop
# {'olma': 5000, 'non': 3000}


# ============================================
# 3-MASHQ: Ikkala dasturni birlashtirish
# Buyurtma ro'yxatidagi har bir mahsulotni
# e-bozor lug'ati bilan solishtirish:
# - mavjud bo'lsa narxini chiqarish
# - mavjud bo'lmasa xabar chiqarish
# ============================================

buyurtmalar = []
while True:
    buyurtma = input("nma buyurtma berasiz?")
    if buyurtma.lower() == "stop":
        break
    buyurtmalar.append(buyurtma)

print(buyurtmalar)

e_bozor = {}
while True:
    nomi = input("Mahsulot nomini kiriting:")
    if nomi == "stop":
        break
    else:
        narx = int(input(f"{nomi} narxi"))
        e_bozor[nomi] = narx

print(e_bozor)

for mahsulot in buyurtmalar:
    if mahsulot in e_bozor:
        print(f"{mahsulot} ,{e_bozor[mahsulot]} som")
    else:
        print("bunday mahsulot yoq")

# Natija (misol):
# nma buyurtma berasiz? olma
# nma buyurtma berasiz? sut
# nma buyurtma berasiz? stop
# ['olma', 'sut']
#
# Mahsulot nomini kiriting: olma
# olma narxi5000
# Mahsulot nomini kiriting: non
# non narxi3000
# Mahsulot nomini kiriting: stop
# {'olma': 5000, 'non': 3000}
#
# olma ,5000 som
# bunday mahsulot yoq
