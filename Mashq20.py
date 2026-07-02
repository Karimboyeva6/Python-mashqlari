def mijoz(ismi, familiyasi, t_yil, t_joy, hozr_yil, e_manzil=None, tel_raq=None):
    yosh = hozr_yil - t_yil
    return {
        "Ism": ismi,
        "Familiya": familiyasi,
        "T_yil": t_yil,
        "Joyi": t_joy,
        "Manzil": e_manzil,
        "Raqam": tel_raq,
        "Yosh": yosh
    }

mijozlar = []

while True:
    ism = input("Ismi:")
    familiya = input("Familiyasi:")
    t_yil = int(input("T_yil:"))
    t_joy = input("T_joy:")
    e_manzil = input("Manzil:")
    tel_raq = input("Raqam:")
    hozr_yil = int(input("Hozirgi yilni kiriting: "))

    if e_manzil == "":
        e_manzil = None
    if tel_raq == "":
        tel_raq = None

    mijozlar.append(mijoz(ism, familiya, t_yil, t_joy, hozr_yil, e_manzil, tel_raq))

    javob = input("Yana mijoz qo'shasizmi? (ha/yo'q): ")
    if javob.lower() != "ha":
        break

for m in mijozlar:
    print(m)

# Natija:
# {'Ism': 'Ali', 'Familiya': 'Valiyev', 'T_yil': 2005,
# 'Joyi': 'Toshkent', 'Manzil': 'ali@gmail.com',
# 'Raqam': '998901234567', 'Yosh': 21}


def kattasi(a, b, c):
    return max(a, b, c)

print(kattasi(2, 5, 6))

# Natija:
# 6


def aylana(radius, pi=3.14):
    return {
        "Radius": radius,
        "Diametr": 2 * radius,
        "Perimetr": 2 * pi * radius,
        "Yuzi": pi * radius ** 2
    }

a = int(input("Radiusni kiriting:"))
print(aylana(a))

# Masalan, radius = 5 bo'lsa:
# {'Radius': 5, 'Diametr': 10, 'Perimetr': 31.4, 'Yuzi': 78.5}


def tub_sonlar(a, b):
    natija = []
    for son in range(a, b + 1):
        if son > 1:
            tub = True
            for i in range(2, son):
                if son % i == 0:
                    tub = False
                    break
            if tub:
                natija.append(son)
    return natija

print(tub_sonlar(1, 20))

# Natija:
# [2, 3, 5, 7, 11, 13, 17, 19]


def fibonacci(x):
    sonlar = []
    a, b = 1, 1
    for i in range(x):
        sonlar.append(a)
        a, b = b, a + b
    return sonlar

x = int(input("Fibonacci son kiriting:"))
print(fibonacci(x))

# Masalan, x = 5 bo'lsa:
# [1, 1, 2, 3, 5]