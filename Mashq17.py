# ============================================================
# 1-MASHQ: Yaxshi ko'rgan kitoblar
# ============================================================
# Foydalanuvchidan yaxshi ko'rgan kitoblarini so'raydigan dastur.
# "stop" yozilganda dastur to'xtaydi.

# while True:
#     kitob = input("Yaxshi korgan kitoblaringizni kiriting: ")
#     if kitob == "stop":
#         break
#     print(f"Mening yaxshi korgan kitobim: {kitob}")

# Natija namunasi:
# Yaxshi korgan kitoblaringizni kiriting: Harry Potter
# Mening yaxshi korgan kitobim: Harry Potter
# Yaxshi korgan kitoblaringizni kiriting: O'tkan kunlar
# Mening yaxshi korgan kitobim: O'tkan kunlar
# Yaxshi korgan kitoblaringizni kiriting: stop
# (dastur to'xtaydi)


# ============================================================
# 2-MASHQ: Muzey chiptasi — 1-usul (oddiy shart, "or" bilan)
# ============================================================
# 7 yoshgacha - 2000 so'm, 7-18 - 3000 so'm, 18-65 - 10000 so'm,
# 65 dan katta - bepul. "exit" yoki "quit" yozilganda dastur to'xtaydi.

# while True:
#     yosh = input("Yoshingizni kiriting: ")
#     if yosh == "exit" or yosh == "quit":
#         break
#     yosh = int(yosh)
#     if yosh < 7:
#         print(2000)
#     elif yosh < 18:
#         print(3000)
#     elif yosh < 65:
#         print(10000)
#     else:
#         print("Bepul")

# Natija namunasi:
# Yoshingizni kiriting: 5
# 2000
# Yoshingizni kiriting: 70
# Bepul
# Yoshingizni kiriting: exit
# (dastur to'xtaydi)


# ============================================================
# 2-MASHQ: Muzey chiptasi — 2-usul (break, alohida shartlar bilan)
# ============================================================

# while True:
#     yosh = input("Yoshingizni kiriting: ")
#     if yosh == "exit":
#         break
#     if yosh == "quit":
#         break
#     yosh = int(yosh)
#     if yosh < 7:
#         print(2000)
#     elif yosh < 18:
#         print(3000)
#     elif yosh < 65:
#         print(10000)
#     else:
#         print("Bepul")

# Natija namunasi:
# Yoshingizni kiriting: 10
# 3000
# Yoshingizni kiriting: quit
# (dastur to'xtaydi)


# ============================================================
# 2-MASHQ: Muzey chiptasi — 3-usul (flag/ishora o'zgaruvchi bilan)
# ============================================================

davom_etish = True

while davom_etish:
    yosh = input("Yoshingizni kiriting: ")
    if yosh == "exit" or yosh == "quit":
        davom_etish = False
    else:
        yosh = int(yosh)
        if yosh < 7:
            print(2000)
        elif yosh < 18:
            print(3000)
        elif yosh < 65:
            print(10000)
        else:
            print("Bepul")

# Natija namunasi:
# Yoshingizni kiriting: 3
# 2000
# Yoshingizni kiriting: 65
# Bepul
# Yoshingizni kiriting: exit
# (dastur to'xtaydi)


# ============================================================
# 3-MASHQ: Ildiz dasturi — xatolari tuzatilgan
# ============================================================
# Asl koddagi mantiqiy xatolar va ularning yechimi:
#   1) input() har doim STRING qaytaradi, shuning uchun avval uni songa
#      (float) aylantirmasdan "qiymat < 0" deb solishtirib bo'lmaydi.
#      -> Yechim: avval exitni tekshirib, keyin float() ga aylantirildi.
#   2) 'Exit' (katta harf bilan) yozilgan edi, foydalanuvchi kichik harfda
#      yozsa ishlamaydi.
#      -> Yechim: qiymat.lower() == 'exit' qilib, katta-kichik harfga
#      bog'liq bo'lmay ishlaydigan qilindi.
#   3) Tartib noto'g'ri edi: manfiy son tekshiruvi exit tekshiruvidan oldin
#      turgani uchun, "exit" so'zini songa aylantirishga urinib xato
#      (ValueError) berardi.
#      -> Yechim: avval exit tekshiriladi, keyin songa aylantiriladi,
#      keyin manfiy son tekshiriladi.

# savol = "Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)

#     if qiymat.lower() == 'exit':
#         break

#     qiymat = float(qiymat)

#     if qiymat < 0:
#         continue
#     else:
#         ildiz = qiymat ** (0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")

# Natija namunasi:
# Musbat son kiriting (dasturni to'xtatish uchun 'exit' deb yozing): 9
# 9.0 ning ildizi 3.0 ga teng
# Musbat son kiriting (dasturni to'xtatish uchun 'exit' deb yozing): -4
# (hech narsa chiqmaydi, qayta so'raydi - continue ishlagani uchun)
# Musbat son kiriting (dasturni to'xtatish uchun 'exit' deb yozing): EXIT
# (dastur to'xtaydi)
