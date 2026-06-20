# 1-MASHQ: DAVLATLAR
davlatlar = ["Saudiya Arabistoni", "Xitoy", "Hindiston", "Yaponiya"]

print("Davlatlar:", davlatlar)
# ['Saudiya Arabistoni', 'Xitoy', 'Hindiston', 'Yaponiya']

print("Elementlar soni:", len(davlatlar))
# 4

print("Sorted:", sorted(davlatlar))
# ['Hindiston', 'Yaponiya', 'Saudiya Arabistoni', 'Xitoy']

print("Reverse sorted:", sorted(davlatlar, reverse=True))
# ['Xitoy', 'Saudiya Arabistoni', 'Yaponiya', 'Hindiston']

print("Asl ro'yxat:", davlatlar)
# ['Saudiya Arabistoni', 'Xitoy', 'Hindiston', 'Yaponiya']

davlatlar.sort()
print("Sort:", davlatlar)
# ['Hindiston', 'Yaponiya', 'Saudiya Arabistoni', 'Xitoy']

davlatlar.sort(reverse=True)
print("Reverse sort:", davlatlar)
# ['Xitoy', 'Saudiya Arabistoni', 'Yaponiya', 'Hindiston']

# 2-MASHQ: JUFT SONLAR
juft_sonlar = list(range(120, 1201, 2))

print("Yig'indi:", sum(juft_sonlar))
# 357000 (120 dan 1200 gacha juft sonlar yig'indisi)

print("Farq:", max(juft_sonlar) - min(juft_sonlar))
# 1080

print("Elementlar soni:", len(juft_sonlar))
# 541

print("Boshidan 5 ta:", juft_sonlar[:5])
# [120, 122, 124, 126, 128]

orta = len(juft_sonlar) // 2
print("O'rtadan 10 ta:", juft_sonlar[orta:orta+10])
# o‘rta qismdagi 10 ta son

print("Oxiridan 5 ta:", juft_sonlar[-5:])
# [1192, 1194, 1196, 1198, 1200]

# 3-MASHQ: TAOMLAR VA NONUSHTA
taomlar = ["Osh", "manti", "sho'rva", "somsa", "xonim"]

nonushta = taomlar[:]

nonushta.remove("Osh")
nonushta.remove("manti")
nonushta.remove("sho'rva")
nonushta.remove("xonim")

nonushta.append("blinchik")
nonushta.append("pankeyk")

print("Taomlar:", taomlar)
# ['Osh', 'manti', 'sho'rva', 'somsa', 'xonim']

print("Nonushta:", nonushta)
# ['somsa', 'blinchik', 'pankeyk']

nonushta = tuple(nonushta)

# ❌ XATO QISM:
# nonushta[0] = "qaymoq", "non"

# 🧠 IZOH:
# Tuple o'zgarmas (immutable), shuning uchun elementni o'zgartirib bo'lmaydi
