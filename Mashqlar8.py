#mashq1
ismlar = ["Qunduz", "Munisa", "Zuhra"]
for ism in ismlar:
    print(f"Salom {ism}, yaxshimisan")

# Natija:
# Salom Qunduz, yaxshimisan
# Salom Munisa, yaxshimisan
# Salom Zuhra, yaxshimisan
#mashq2
sonlar = [4, -5, 1.3]
print(sum(sonlar))
sonlar.insert(1, 56)
print(sonlar)

# Natija:
# 0.3000000000000007
# [4, 56, -5, 1.3]
#mashq3
t_shaxslar = ["Zahriddin Muhammad Bobur", "Alisher Navoiy", "Jaloliddin Manguberdi"]
z_shaxslar = ["Islom Karimov", "Abduqodir Xusanov", " Ranaldo"]
tarixiy = t_shaxslar.pop()
zamonaviy = z_shaxslar.pop()
print(f'Men eng hurmat qiladigan tarixiy shaxs:{tarixiy}')
print(f'Men hurmat qiladigan zamonaviy shaxs:{zamonaviy}')
print(f"Qolgan tarixiy shaxslar:{t_shaxslar}")
print(f"Qolgan zamonaviy shaxslar:{z_shaxslar}")

# Natija:
# Men eng hurmat qiladigan tarixiy shaxs:Jaloliddin Manguberdi
# Men hurmat qiladigan zamonaviy shaxs: Ranaldo
# Qolgan tarixiy shaxslar:['Zahriddin Muhammad Bobur', 'Alisher Navoiy']
# Qolgan zamonaviy shaxslar:['Islom Karimov', 'Abduqodir Xusanov']
#mashq4
mehmonlar = []
mehmonlar.append("Munisa")
mehmonlar.append("Sevinch")
mehmonlar.append("Zuhra")
mehmonlar.append("Osiyo")
mehmonlar.append("Orifjon")
print("Mehmonlar royhati:", mehmonlar)
mehmonlar.remove("Munisa")
print("Munisa kela olmaydi", mehmonlar)
mehmonlar.insert(0, "Umida")
mehmonlar.append("Matluba")
orta = len(mehmonlar) // 2
mehmonlar.insert(orta, " Shaxnoza")
print(f"yangi mehmonlar qoshilgandan keyin, {mehmonlar}")
yangi_mehmonlar = []
for x in range(3):
    kelgan_mehmon = mehmonlar.pop()
    yangi_mehmonlar.append(kelgan_mehmon)
print("mehmonga kelganlar royhati:", yangi_mehmonlar)
print("hali kelmagan mehmonlar:", mehmonlar)

# Natija:
# Mehmonlar royhati: ['Munisa', 'Sevinch', 'Zuhra', 'Osiyo', 'Orifjon']
# Munisa kela olmaydi ['Sevinch', 'Zuhra', 'Osiyo', 'Orifjon']
# yangi mehmonlar qoshilgandan keyin, ['Umida', 'Sevinch', ' Shaxnoza', 'Zuhra', 'Osiyo', 'Orifjon', 'Matluba']
# mehmonga kelganlar royhati: ['Matluba', 'Orifjon', 'Osiyo']
# hali kelmagan mehmonlar: ['Umida', 'Sevinch', ' Shaxnoza', 'Zuhra']
