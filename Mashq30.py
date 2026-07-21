import json

# 1-mashq
data = {
    "Model": "Malibu",
    "Rang": "Qora",
    "Yil": 2020,
    "Narh": 40000
}

json_matn = json.dumps(data)
print(json_matn)

# Natija:
# Python lug'ati JSON matniga aylantirildi.
# JSON matni konsolga chiqarildi.
# Chiqish:
# {"Model": "Malibu", "Rang": "Qora", "Yil": 2020, "Narh": 40000}


# 2-mashq
talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""

json_mal = json.loads(talaba_json)

print(json_mal["ism"], json_mal["familiya"])

# Natija:
# JSON matni Python lug'atiga aylantirildi.
# Talabaning ismi va familiyasi konsolga chiqarildi.
# Chiqish:
# Hasan Husanov


# 3-mashq
with open("data.json", "w") as f:
    json.dump(data, f)

with open("talaba.json", "w") as f:
    json.dump(json_mal, f)

# Natija:
# data.json fayli yaratildi.
# talaba.json fayli yaratildi.
# Ma'lumotlar JSON formatida fayllarga muvaffaqiyatli saqlandi.


# 4-mashq
with open("students.json", "r") as f:
    student_json = json.load(f)

for talaba in student_json["student"]:
    print(f"{talaba['name']} {talaba['lastname']}, {talaba['year']}-Kurs, {talaba['faculty']} talabasi")

# Natija:
# students.json fayli o'qildi.
# Barcha talabalar ekranga chiqarildi.
#
# Chiqish:
# Tom Price, 4-Kurs, Engineering talabasi
# Nick Thameson, 3-Kurs, Computer Science talabasi
# John Doe, 2-Kurs, ICT talabasi


# 5-mashq
with open("Wikipedia.json", "r") as f:
    malumot = json.load(f)

print(malumot["query"]["pages"]["13801"]["title"])
print(malumot["query"]["pages"]["13801"]["extract"])

# Natija:
# Wikipedia.json fayli o'qildi.
# Maqolaning sarlavhasi (title) va qisqacha mazmuni (extract) konsolga chiqarildi.
#
# Chiqish:
# Python
# Python dasturlash tili haqida qisqacha ma'lumot konsolga chiqarildi.