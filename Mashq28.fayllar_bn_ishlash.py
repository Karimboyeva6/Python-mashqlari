# Faylga yozish rejimida ("w") ochamiz — agar fayl bo'lmasa, yangi yaratiladi
with open("bugungi_dars.txt", "w") as f:
    f.write("Bugun men quyidagilarni o'rgandim:\n")
    f.write("- Fayllar bilan ishlash (open, read, write)\n")
    f.write("- Matn ichidan qism-satr qidirish\n")
    f.write("- Pickle moduli yordamida ma'lumot saqlash\n")

# Xuddi shu faylni o'qish rejimida ("r") ochib, mazmunini tekshiramiz
with open("bugungi_dars.txt", "r") as f:
    matn = f.read()

print(matn)  # Natija: fayldagi 4 qatorli matn ekranga chiqadi


# 30 xonali pi.txt faylini o'qish rejimida ochamiz
with open('pi.txt') as fayl:
    pi = fayl.read()          # Faylning butun mazmunini matn sifatida olamiz

pi = pi.rstrip()               # Oxiridagi ortiqcha bo'shliq/enter belgilarini olib tashlaymiz
pi = pi.replace('\n', '')      # Qator ichidagi barcha \n belgilarini olib tashlaymiz
pi = float(pi)                 # Endi toza matnni o'nlik songa (float) aylantiramiz

print(pi)  # Natija: 3.141592653589793 (Python float faqat ~15-17 xonani saqlaydi)

import os
import urllib.request

yol = "/storage/emulated/0/pi_million_digits.txt"
url = "https://raw.githubusercontent.com/ehmatthes/pcc_2e/master/chapter_10/pi_million_digits.txt"

# Agar fayl hali yuklanmagan bo'lsa, internetdan yuklab olamiz
if not os.path.exists(yol):
    urllib.request.urlretrieve(url, yol)

# Faylni o'qib, matnni tozalaymiz
with open(yol) as fayl:
    pi_million = fayl.read()

pi_million = pi_million.rstrip()
pi_million = pi_million.replace('\n', '')  # Barcha qator o'tishlarini olib tashlaymiz

# Tug'ilgan kun ketma-ketligi pi ichida bor-yo'qligini tekshiruvchi funksiya
def check_birthday(pi_matn, tugilgan_kun):
    return tugilgan_kun in pi_matn   # "in" operatori qism-satr borligini tekshiradi

tugilgan_kun = "09102005"  # Tug'ilgan sana: 09.10.2005
natija = check_birthday(pi_million, tugilgan_kun)
print(natija)  # True yoki False

import pickle

# Million xonali matnning dastlabki 100 ta raqamini olib, float songa aylantiramiz
# (to'liq million xonani float qilib bo'lmaydi, chunki Python float ~15-17 xonagacha aniqlikni saqlaydi)
pi_float = float("3." + pi_million[0:100])
print(pi_float)

# pi_float qiymatini pickle formatida binary faylga saqlaymiz
with open('pi_million.pickle', 'wb') as fayl:   # 'wb' — write binary
    pickle.dump(pi_float, fayl)

# Saqlangan qiymatni qayta o'qib, to'g'ri saqlanganini tekshiramiz
with open('pi_million.pickle', 'rb') as fayl:   # 'rb' — read binary
    yangi = pickle.load(fayl)

print(yangi)  # pi_float bilan bir xil qiymat chiqishi kerak