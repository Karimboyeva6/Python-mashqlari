#1-mashq
onam = {"ismi": "Gavhar",
"tugilgan_yili": 1976,
"shahri":  "Qoraqalpoģiston Res"}
print(f'Onamning ismi {onam["ismi"]}, {onam["tugilgan_yili"]} da {onam["shahri"]} da  tugilgan')

# NATIJA:
# Onamning ismi Gavhar, 1976 da Qoraqalpoģiston Res da  tugilgan

#2-mashq 
sevimli_taomlar = {"Gavhar": "kartoshka_barak",
"Saporboy": "beshbarmoq",
"Yulduz": "tuxum_barak",
"Qunduz": "manti",
"Durdona": "kartoshka_barak"}
print(f'dadamning sevimli taomi {sevimli_taomlar["Saporboy"]}, onamniki {sevimli_taomlar["Gavhar"]}, egizimniki {sevimli_taomlar["Qunduz"]}')

# NATIJA:
# dadamning sevimli taomi beshbarmoq, onamniki kartoshka_barak, egizimniki manti

#3-mashq
atamalar = {"integer": "butun son",
"string": "matn",
"float": "kasr son",
"boolean": "mantiqiy qiymat",
"complex": "murakkab son",
"if": "agar",
"else": "aks holda",
"for": "uchun",
"loop": "sikl",
"def": "funksiya"}
print(atamalar)

# NATIJA:
# {'integer': 'butun son', 'string': 'matn', 'float': 'kasr son', 'boolean': 'mantiqiy qiymat',
#  'complex': 'murakkab son', 'if': 'agar', 'else': 'aks holda', 'for': 'uchun',
#  'loop': 'sikl', 'def': 'funksiya'}

#4-mashq
atamalar = {"integer": "butun son",
"string": "matn",
"float": "kasr son",
"boolean": "mantiqiy qiymat",
"complex": "murakkab son",
"if": "agar",
"else": "aks holda",
"for": "uchun",
"loop": "sikl",
"def": "funksiya"}
print(atamalar)

soz =input("soz kiriting:")

if soz in atamalar:
  print(f"bu sozning {soz} tarjimasi {atamalar[soz]}")
else:
  print("bu soz mavjud emas")

# NATIJA (misol uchun "integer" kiritilganda):
# soz kiriting: integer
# bu sozning integer tarjimasi butun son

# NATIJA (misol uchun lug'atda yo'q so'z kiritilganda, masalan "class"):
# soz kiriting: class
# bu soz mavjud emas
