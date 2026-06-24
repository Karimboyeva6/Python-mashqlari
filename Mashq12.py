# =========================================================
# 1-misol: kiritilgan sonning juft yoki tokligini tekshiradi
# =========================================================
son = int(input("Juft son kiriting:"))
if son % 2 == 0:
    print("Rahmat!")
else:
    print("Bu son juft emas")

# Masalan: son=8  -> "Rahmat!"
#          son=7  -> "Bu son juft emas"


# =========================================================
# 2-misol: yosh bo'yicha muzeyga kirish narxini aniqlaydi
# =========================================================
yosh = int(input("Yoshingiz nechada?"))
if yosh < 4 or yosh > 60:
    print("sizga muzeyga kirish bepul")
elif yosh < 18:
    print('sizga kirish 10000 som')
else:
    print('20000 som')

# Masalan: yosh=3   -> "sizga muzeyga kirish bepul"
#          yosh=65  -> "sizga muzeyga kirish bepul"
#          yosh=15  -> "sizga kirish 10000 som"
#          yosh=30  -> "20000 som"


# =========================================================
# 3-misol: ikki sonni solishtirish (qaysi biri katta yoki teng)
# Asl kodda xato bor edi: "if" qatori ortiqcha bo'sh joy bilan boshlangan
# va "elif...print" bitta qatorga yozilgan edi - shu sabab xato chiqardi.
# =========================================================
son1 = int(input('birinchi sonni kiriting:'))
son2 = int(input('ikkinchi sonni kiriting:'))

if son1 > son2:
    print("birinchi son katta")
elif son1 < son2:
    print("ikkinchi son katta")
else:
    print("ikkala son teng")

# Masalan: son1=10, son2=5 -> "birinchi son katta"
#          son1=3,  son2=8 -> "ikkinchi son katta"
#          son1=4,  son2=4 -> "ikkala son teng"


# =========================================================
# 4-misol: foydalanuvchi kiritgan mahsulotlarni doʻkon roʻyxati bilan tekshiradi
# Asl kodda "else:" qatori ortiqcha bo'sh joy bilan yozilgan edi (xato).
# =========================================================
mahsulotlar = ["olma", "banan", "gilos", "olcha", "murabbo", "olxoʻri", "uzum", "ananas", "tut", "shaftoli"]
yangi_savat = []

for x in range(5):
    mahsulot = input(f"Savatga {x+1}ta mahsulot kiriting:")
    yangi_savat.append(mahsulot)

for a in yangi_savat:
    if a in mahsulotlar:
        print(a, "- Mahsulot dokonimizda bor")
    else:
        print(a, "- Mahsulot dokonimizda yoʻq")

# Masalan: foydalanuvchi "olma" kiritsa -> "olma - Mahsulot dokonimizda bor"
#          foydalanuvchi "kartoshka" kiritsa -> "kartoshka - Mahsulot dokonimizda yoʻq"


# =========================================================
# 5-misol: mahsulotlarni "bor" va "yoʻq" roʻyxatlarga ajratadi
# Asl kodda "if/else" bloklari for ichida indentatsiyasiz yozilgan edi (xato),
# shuningdek yakuniy if/else ham for tashqarisida bo'lishi kerak edi.
# =========================================================
mahsulotlar = ["olma", "banan", "olcha", "gilos", "uzum"]
bor_mahsulotlar = []
yoʻq_mahsulotlar = []

for x in range(5):
    mahsulot = input(f"{x+1} mahsulot kiriting: ")
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        yoʻq_mahsulotlar.append(mahsulot)

if len(yoʻq_mahsulotlar) == 0:
    print("siz soʻragan barcha mahsulotlar dokonimizda bor:", bor_mahsulotlar)
else:
    print("quyidagi mahsulotlar dokonimizda yoʻq:", yoʻq_mahsulotlar)

# Masalan: barcha kiritilgan mahsulotlar roʻyxatda bo'lsa
#   -> "siz soʻragan barcha mahsulotlar dokonimizda bor: [...]"
# aks holda
#   -> "quyidagi mahsulotlar dokonimizda yoʻq: [...]"


# =========================================================
# 6-misol: yangi login mavjud foydalanuvchilar roʻyxatida bor-yo'qligini tekshiradi
# Asl kodda if/else bloklari indentatsiyasiz yozilgan edi (xato).
# =========================================================
foydalanuvchilar = ["Ali", "vali", "olim", "anvar", "kozim"]
login = input("Yangi login kiriting:")

if login in foydalanuvchilar:
    print("Login band yangi login tanlang!")
else:
    print("Xush kelibsiz, foydalanuvchi!")

# Masalan: login="vali" -> "Login band yangi login tanlang!"
#          login="javlon" -> "Xush kelibsiz, foydalanuvchi!"
# Eslatma: ro'yxatda "Ali" katta harf bilan, lekin "vali" kichik harf bilan -
# Python katta-kichik harfni farqlaydi (case-sensitive), shuni hisobga oling.


# =========================================================
# 7-misol: berilgan butun sonning 2 dan 10 gacha bo'lgan sonlarga bo'linishini tekshiradi
# Asl kodda "if print" qatorlari for ichida indentatsiyasiz yozilgan edi (xato).
# =========================================================
butun_son = int(input("butun son kiriting:"))

for son in range(2, 11):
    if butun_son % son == 0:
        print(f"{butun_son} soni {son} ga qoldiqsiz boʻlinadi")

# Masalan: butun_son=12 -> 
# "12 soni 2 ga qoldiqsiz boʻlinadi"
# "12 soni 3 ga qoldiqsiz boʻlinadi"
# "12 soni 4 ga qoldiqsiz boʻlinadi"
# "12 soni 6 ga qoldiqsiz boʻlinadi"
