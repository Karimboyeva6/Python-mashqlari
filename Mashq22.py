def kopaytir(*son):
    x = 1
    for s in son:
            x =x * s
    return x 
print(kopaytir(1, 2, 3, 4, 5))
# Natija: 120


def talabalar(ismi, familiyasi, **malumot):
  natija = {}
  natija["ismi"] = ismi
  natija["familiyasi"] = familiyasi
  natija.update(malumot)
  return natija
print(talabalar("Yulduz", "Karimboyeva", yoshi = 21, yili = 2005))
# Natija: {'ismi': 'Yulduz', 'familiyasi': 'Karimboyeva', 'yoshi': 21, 'yili': 2005}