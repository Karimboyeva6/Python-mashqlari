# Avto klassi

class Avto:
    def init(self, model, rang, korobka, narx):
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narx = narx
        self.kilometr = 0

    def get_model(self):
        return self.model

    def get_rang(self):
        return self.rang

    def get_narx(self):
        return self.narx

    def get_info(self):
        return f"Mashina Modeli: {self.model}, Rangi: {self.rang}, Korobkasi: {self.korobka}, Narxi: {self.narx}, Yurgani: {self.kilometr} km"

    def update_rang(self, yangi_rang):
        self.rang = yangi_rang

    def update_km(self, km):
        if km >= self.kilometr:
            self.kilometr = km
        else:
            print("Kilometrni kamaytirib bo'lmaydi!")

    def update_narx(self, yangi_narx):
        self.narx = yangi_narx

    def update_korobka(self, yangi_korobka):
        self.korobka = yangi_korobka

# Natija:
# Avto klassi yaratildi.
# Avtomobilning modeli, rangi, korobkasi, narxi va kilometri saqlandi.
# Getter metodlari orqali ma'lumotlar olindi.
# update_km() metodi yordamida kilometr yangilandi.
# get_info() metodi avtomobil haqida to'liq ma'lumot qaytardi.


# Avtosalon klassi

class Avtosalon:
    def init(self, salon_nomi, manzili):
        self.salon_nomi = salon_nomi
        self.manzili = manzili
        self.avtolar = []

    def add_avto(self, avto):
        self.avtolar.append(avto)

    def get_avtolar_info(self):
        malumotlar = ""
        for avto in self.avtolar:
            malumotlar += avto.get_info() + "\n"
        return malumotlar

# Natija:
# Avtosalon klassi yaratildi.
# Salon nomi, manzili va avtomobillar ro'yxati saqlandi.
# add_avto() metodi orqali yangi avtomobillar salonga qo'shildi.
# get_avtolar_info() metodi salondagi avtomobillar haqida ma'lumot qaytardi.


# Obyektlar yaratish

salon1 = Avtosalon("Uzavto", "Toshkent")
salon2 = Avtosalon("Xorazmavto", "Xorazm")

avto1 = Avto("Damas", "qora", "mexanika", 12000)
avto2 = Avto("Cobalt", "oq", "avto", 20000)

salon1.add_avto(avto1)
salon2.add_avto(avto2)

print("1-salon avtomobillari")
print(salon1.get_avtolar_info())

print("2-salon avtomobillari")
print(salon2.get_avtolar_info())

# Natija:
# 1-salon avtomobillari
# Mashina Modeli: Damas, Rangi: qora, Korobkasi: mexanika,
# Narxi: 12000, Yurgani: 0 km
#
# 2-salon avtomobillari
# Mashina Modeli: Cobalt, Rangi: oq, Korobkasi: avto,
# Narxi: 20000, Yurgani: 0 km


# dir() funksiyasi

print(dir(Avto))
print(dir(Avtosalon))

# Natija:
# Avto va Avtosalon klasslarining barcha metodlari
# hamda xususiyatlari ekranga chiqarildi.


# dict metodi

print(avto1.dict)
print(salon1.dict)

# Natija:
# Obyektlarning barcha atributlari va ularning qiymatlari
# lug'at (dictionary) ko'rinishida chiqarildi.


# Pythonning tayyor klasslari

print(dir(str))
print(dir(int))
print(dir(list))

# Natija:
# str, int va list klasslarining mavjud metodlari va
# xususiyatlari dir() funksiyasi yordamida ko'rildi.