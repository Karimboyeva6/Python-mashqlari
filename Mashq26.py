class Shaxs:
    odamlar_soni = 0

    def __init__(self, ism, familiya, passport):
        self.ism = ism
        self.familiya = familiya
        self.__passport = passport
        Shaxs.odamlar_soni += 1

    def get_info(self):
        return f"Ismi: {self.ism}, Familiyasi: {self.familiya}"

    def get_passport(self):
        return f"Foydalanuvchining passporti: {self.__passport}"

    def set_passport(self, yangi_passport):
        self.__passport = yangi_passport

    @classmethod
    def get_odamlar_soni(cls):
        return cls.odamlar_soni

# Natija:
# Shaxs klassiga __passport nomli yopiq xususiyat qo'shildi.
# get_passport() va set_passport() metodlari orqali passport ma'lumotini
# ko'rish va o'zgartirish imkoniyati yaratildi.
# odamlar_soni klass atributi qo'shildi.
# get_odamlar_soni() klass metodi orqali yaratilgan shaxslar soni olindi.


class Talaba(Shaxs):
    talabalar_soni = 0

    def __init__(self, ism, familiya, passport, bosqich, id_raqam):
        super().__init__(ism, familiya, passport)
        self.bosqich = bosqich
        self.fanlar = []
        self.__id_raqam = id_raqam
        Talaba.talabalar_soni += 1

    def fanga_yozil(self, fan):
        self.fanlar.append(fan)

    def remove_fan(self, fan):
        if fan in self.fanlar:
            self.fanlar.remove(fan)
        else:
            return "Siz bu fanga yozilmagansiz"

    def get_info(self):
        return f"Ismi: {self.ism}, Familiyasi: {self.familiya}, Bosqichi: {self.bosqich}, Fanlar soni: {len(self.fanlar)}"

    def get_id_raqam(self):
        return f"Foydalanuvchining ID raqami: {self.__id_raqam}"

    def set_id_raqam(self, yangi_id):
        self.__id_raqam = yangi_id

    @classmethod
    def get_talabalar_soni(cls):
        return cls.talabalar_soni

# Natija:
# Talaba klassiga __id_raqam nomli yopiq xususiyat qo'shildi.
# get_id_raqam() va set_id_raqam() metodlari yaratildi.
# talabalar_soni klass atributi qo'shildi.
# get_talabalar_soni() klass metodi orqali talabalar soni olindi.


# Obyektlar yaratish

shaxs1 = Shaxs("Ali", "Valiyev", "AA1234567")
talaba1 = Talaba("Hasan", "Karimov", "AB7654321", 2, "ID001")
talaba2 = Talaba("Vali", "Aliyev", "AC1122334", 3, "ID002")

# Natija:
# 1 ta Shaxs va 2 ta Talaba obyekti yaratildi.


# Natijalarni tekshirish

print(shaxs1.get_passport())
print(talaba1.get_id_raqam())

print(Shaxs.get_odamlar_soni())
print(Talaba.get_talabalar_soni())

# Natija:
# Foydalanuvchining passporti: AA1234567
# Foydalanuvchining ID raqami: ID001
# Jami yaratilgan shaxslar soni: 3
# Jami yaratilgan talabalar soni: 2