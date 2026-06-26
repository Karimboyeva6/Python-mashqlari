Xatolar ustida ishlash
# MASHQ 1: Juft/toq sonni aniqlash
# ==========================================

# XATO KOD:
# son = float(input("Juft son kiriting: ")   # qavs yopilmagan
# if son%2==0:
# print("Bu son juft emas.')                 # tirnoqlar mos emas, mantiq teskari
# else:
# print("Rahmat!"))                          # ortiqcha qavs

# TO'G'RI KOD:
son = float(input("Juft son kiriting: "))
if son % 2 == 0:
    print("Bu juft son")
else:
    print("Bu juft son emas")


# ==========================================
# MASHQ 2: Chipta narxini hisoblash
# ==========================================

# XATO KOD:
# yosh = (input("Yoshingiz nechida?"))   # int() ga o'tkazilmagan
# if yosh<=4 or yosh>=60:
# narh = 0                                # indentatsiya yo'q
# elif yosh < 18                          # ":" yetishmaydi
# narh = 10000
# else:
# narh = 20000
# print(f"Chipta {narh} so'm")

# TO'G'RI KOD:
yosh = int(input("Yoshingiz nechida? "))
if yosh <= 4 or yosh >= 60:
    narh = 0
elif yosh < 18:
    narh = 10000
else:
    narh = 20000
print(f"Chipta {narh} so'm")


# ==========================================
# MASHQ 3: Ikki sonni solishtirish
# ==========================================

# XATO KOD:
# x = float(input("Birinchi sonni kiriting: ")    # qavs yopilmagan
# y = float(input("Ikkinchi sonni kiriting: ")    # qavs yopilmagan
# if x==y:
# print(f"{x}={y}")                               # indentatsiya yo'q
# elif x<y:
# print(f'{x}<{y}")                               # tirnoqlar mos emas
# else                                             # ":" yetishmaydi
# print(f"{x}>{y}")

# TO'G'RI KOD:
x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting: "))
if x == y:
    print(f"{x} = {y}")
elif x < y:
    print(f"{x} < {y}")
else:
    print(f"{x} > {y}")


# ==========================================
# MASHQ 4: Savatdagi mahsulotlarni tekshirish (oddiy)
# ==========================================

# XATO KOD:
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
# 'kartoshka', 'olma', 'banan', 'uzum', 'qovun'   # ro'yxat yopilmagan
# for n in range(5):
# savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))  # "savat" e'lon qilinmagan
# if savat:
# for mahsulot in savat                           # ":" yetishmaydi
# if mahsulot in mahsulotlar:
# print(f"Do'konimizda {mahsulot} bor")
# else:
# print(f"Do'konimizda {mahsulot} yo'q")
# else:
# print("Savatingiz bo'sh")

# TO'G'RI KOD:
mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

if savat:
    for mahsulot in savat:
        if mahsulot in mahsulotlar:
            print(f"Do'konimizda {mahsulot} bor")
        else:
            print(f"Do'konimizda {mahsulot} yo'q")
else:
    print("Savatingiz bo'sh")


# ==========================================
# MASHQ 5: Savatdagi mahsulotlar (mavjud emaslar ro'yxati bilan)
# ==========================================

# XATO KOD:
# savat.append(input(f'Savatga {n+1}-mahsulotni qo'shing: '))   # f-string ichida tirnoq to'qnashadi
# bor_mahsulotlar.append(mahslot)                                 # "mahslot" imlo xato
# (indentatsiya yo'qligi sabab boshqa qatorlar ham xato)

# TO'G'RI KOD:
mahsulotlar2 = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
savat2 = []
for n in range(5):
    savat2.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat2:
    if mahsulot in mahsulotlar2:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
    print("Do'konimizda quyidagi mahsulotlar yo'q:")
    for mahsulot in mavjud_emas:
        print(mahsulot)
else:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")


# ==========================================
# MASHQ 6: Login band yoki bo'sh ekanligini tekshirish
# ==========================================

# XATO KOD:
# users = ['alisher1983','aziza','yasina' 'umar']   # vergul yo'q, so'zlar qo'shilib qoladi
# login = input("Yangi login tanlang:' )             # tirnoqlar mos emas
# if login in users:
# print('Login band, yangi login tanalng!')           # indentatsiya yo'q, imlo xato
# else:
# print("Xush kelibsiz!")

# TO'G'RI KOD:
users = ['alisher1983', 'aziza', 'yasina', 'umar']
login = input("Yangi login tanlang: ")
if login in users:
    print("Login band, yangi login tanlang!")
else:
    print("Xush kelibsiz!")


# ==========================================
# MASHQ 7: Sonning bo'linuvchilarini topish
# ==========================================

# XATO KOD:
# son = int(input("Istalgan butun son kiriting: "))
# for n in range(2,11):
# if not (son%n):                                  # indentatsiya yo'q
# print(f"{son} soni {n} ga qoldiqsiz bo'linadi")  # indentatsiya yo'q

# TO'G'RI KOD:
son2 = int(input("Istalgan butun son kiriting: "))
for n in range(2, 11):
    if not (son2 % n):
        print(f"{son2} soni {n} ga qoldiqsiz bo'linadi")
