# 1-mashq

mevalar = ['olma', 'banan', 'olcha', 'gilos', 'qulupnay']

def qaytar(m):
    for i in range(len(m)):
        m[i] = m[i].title()

qaytar(mevalar)
print(mevalar)

# Natija:
# ['Olma', 'Banan', 'Olcha', 'Gilos', 'Qulupnay']
# 2-mashq

mevalar = ['olma', 'banan', 'olcha', 'gilos', 'qulupnay']

def qaytar(m):
    yangi_mevalar = []

    for i in m:
        yangi_mevalar.append(i.title())

    return yangi_mevalar

yangi_mevalar = qaytar(mevalar)

print(mevalar)
print(yangi_mevalar)

# Natija:
# ['olma', 'banan', 'olcha', 'gilos', 'qulupnay']
# ['Olma', 'Banan', 'Olcha', 'Gilos', 'Qulupnay']
# 3-mashq

def bahola(ismlar):
    baholar = {}

    for i in ismlar:
        baho = int(input(f"Talaba {i.title()}ning bahosini kiriting: "))
        baholar[i] = baho

    return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']

baholar = bahola(talabalar)

print(baholar)

# Namuna:
# Talaba Alining bahosini kiriting: 5
# Talaba Valining bahosini kiriting: 4
# Talaba Hasanning bahosini kiriting: 5
# Talaba Husanning bahosini kiriting: 3
#
# Natija:
# {'ali': 5, 'vali': 4, 'hasan': 5, 'husan': 3}