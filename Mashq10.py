#1-mashq
ismlar = ["Yulduz", "Qunduz", "Rano", "Dilnura", "Durdona"]
hisobla = 0
for ism in ismlar:
    print(f"Salom {ism}")
    hisobla += 1
print(f"Kod {hisobla} marta takrorlandi")

# Natija:
# Salom Yulduz
# Salom Qunduz
# Salom Rano
# Salom Dilnura
# Salom Durdona
# Kod 5 marta takrorlandi

#2-mashq
toq_sonlar = range(11, 100, 2)
for son in toq_sonlar:
    print(son ** 3)

# Natija (har bir toq sonning kubi, alohida qatordan):
# 1331
# 2197
# 3375
# ...
# 970299

#3-mashq
kinolar = []
for x in range(5):
    kino = input("Sevimli kinongiz qaysi? ")
    kinolar.append(kino)

print(f"Mening sevimli kinolarim: {kinolar}")

# Natija (misol):
# Sevimli kinongiz qaysi? Yashil maskan
# Sevimli kinongiz qaysi? Novda
# Sevimli kinongiz qaysi? Asl gozallik
# Sevimli kinongiz qaysi? Vatan
# Sevimli kinongiz qaysi? Dil
# Mening sevimli kinolarim: ['Yashil maskan', 'Novda', 'Asl gozallik', 'Vatan', 'Dil']

#4-mashq
suhbat = int(input("Bugun nechta odam bilan suhbatlashdingiz?:"))
ismlar = []
for x in range(suhbat):
    ism = input("Ularning ismlari nima?:")
    ismlar.append(ism)
print(ismlar)

# Natija (misol):
# Bugun nechta odam bilan suhbatlashdingiz?:3
# Ularning ismlari nima?:Sevinch
# Ularning ismlari nima?:Zuxra
# Ularning ismlari nima?:Begoyim
# ['Sevinch', 'Zuxra', 'Begoyim']
