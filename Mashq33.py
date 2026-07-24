"""
Uy ishi: sana, vaqt, regex bilan ishlash mashqlari
"""

import datetime
from dateutil.relativedelta import relativedelta
import re


# ============================================================
# 1-topshiriq: Bugungi sanadan boshlab 2 hafta farq bilan
# 10 ta sanani konsolga chiqarish
# ============================================================

bugun = datetime.date.today()
for x in range(10):
    sana = bugun + datetime.timedelta(weeks=2 * (x + 1))
    print(sana)

# Natija (2026-yil 24-iyuldan boshlab, misol uchun):
# 2026-08-07
# 2026-08-21
# 2026-09-04
# 2026-09-18
# 2026-10-02
# 2026-10-16
# 2026-10-30
# 2026-11-13
# 2026-11-27
# 2026-12-11


# ============================================================
# 2-topshiriq: Ramazon va Qurbon hayitigacha qolgan kunlar
# ============================================================

bugun = datetime.date.today()
ramazon_tax = datetime.date(2027, 3, 10)
qurbon_tax = datetime.date(2027, 5, 27)

qoldi_ramazon = ramazon_tax - bugun
qoldi_qurbon = qurbon_tax - bugun

print(qoldi_ramazon.days)
print(qoldi_qurbon.days)

# Natija (2026-yil 24-iyuldan hisoblanganda):
# Ramazon hayitigacha: 229 kun
# Qurbon hayitigacha: 307 kun


# ============================================================
# 3-topshiriq: Tug'ilgan kundan bugungi sanagacha
# necha yil, oy, kun o'tganini qaytaruvchi funksiya
# ============================================================

def yosh_hisobla(tugilgan_kun):
    bugun = datetime.date.today()
    farq = relativedelta(bugun, tugilgan_kun)
    return farq.years, farq.months, farq.days


natija = yosh_hisobla(datetime.date(2005, 10, 9))
print(f"{natija[0]} yil, {natija[1]} oy, {natija[2]} kun")

# Natija:
# 20 yil, 9 oy, 15 kun


# ============================================================
# 4-topshiriq: Foydalanuvchidan telefon raqamini kiritishni
# so'rash va uni andoza (regex) yordamida tekshirish
# ============================================================

raqam = input("Telefon raqamingizni kiriting (+998XXXXXXXXX): ")
andoza = r'^\+998\d{9}$'

if re.fullmatch(andoza, raqam):
    print("To'g'ri raqam")
else:
    print("Noto'g'ri format")

# Natija (masalan +998944562576 kiritilsa):
# To'g'ri raqam


# ============================================================
# 5-topshiriq: Berilgan matndan veb-sahifa manzilini
# ajratib oluvchi funksiya
# ============================================================

matn = """Quyidagi matndan namuna sifatida foydalanishingiz mumkin:

Assalom alaykum hurmatli do'stlar. Navbatdagi darsimiz YouTubega yuklandi: https://youtu.be/vsxJPRLXpgI

Ushbu darsimizda unittest moduli yordamida klasslarning xususiyatlar va metodlarini tekshiruvchi dastur yozishni o'rganamiz. Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test"""

andoza = r'https://\S+'
natija = re.findall(andoza, matn)
print(natija)

# Natija:
# ['https://youtu.be/vsxJPRLXpgI', 'https://python.sariq.dev/testing/37-klass-test']
