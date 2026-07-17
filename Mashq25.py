class Shaxs:
    def __init__(self, ism, familiya):
        self.ism = ism
        self.familiya = familiya

    def get_info(self):
        return f"Ismi: {self.ism}, Familiyasi: {self.familiya}"


# Natija:
# Shaxs klassi yaratildi.
# Ism va familiya atributlari saqlandi.
# get_info() metodi shaxs haqida ma'lumot qaytardi.


class Talaba(Shaxs):
    def __init__(self, ism, familiya, bosqich):
        super().__init__(ism, familiya)
        self.bosqich = bosqich
        self.fanlar = []

    def fanga_yozil(self, fan):
        self.fanlar.append(fan)

    def remove_fan(self, fan):
        if fan in self.fanlar:
            self.fanlar.remove(fan)
        else:
            return "Siz bu fanga yozilmagansiz"

    def get_info(self):
        return f"Ismi: {self.ism}, Familiyasi: {self.familiya}, Bosqichi: {self.bosqich}, Fanlar soni: {len(self.fanlar)}"


# Natija:
# Talaba klassi yaratildi.
# Talaba fanlarga yozilishi va fanlarni ro'yxatdan o'chirishi mumkin.
# get_info() metodi talaba haqida to'liq ma'lumot qaytardi.


class Fan:
    def __init__(self, fan, oqituvchi):
        self.fan = fan
        self.oqituvchi = oqituvchi

    def get_info(self):
        return f"Fan: {self.fan}, Oqituvchi: {self.oqituvchi}"


# Natija:
# Fan klassi yaratildi.
# Fan nomi va o'qituvchisi saqlandi.
# get_info() metodi fan haqida ma'lumot qaytardi.


class Professor(Shaxs):
    def __init__(self, ism, familiya, ish_staji):
        super().__init__(ism, familiya)
        self.ish_staji = ish_staji

    def get_info(self):
        return f"Ismi: {self.ism}, Familiyasi: {self.familiya}, Ish staji: {self.ish_staji}"


# Natija:
# Professor klassi yaratildi.
# Professorning ish staji saqlandi.
# get_info() metodi professor haqida ma'lumot qaytardi.


class Foydalanuvchi(Shaxs):
    def __init__(self, ism, familiya, login):
        super().__init__(ism, familiya)
        self.login = login

    def get_info(self):
        return f"Ismi: {self.ism}, Familiyasi: {self.familiya}, Login: {self.login}"


# Natija:
# Foydalanuvchi klassi yaratildi.
# Login ma'lumoti saqlandi.
# get_info() metodi foydalanuvchi haqida ma'lumot qaytardi.


class Admin(Foydalanuvchi):
    def __init__(self, ism, familiya, login):
        super().__init__(ism, familiya, login)

    def ban_user(self):
        return "Foydalanuvchi bloklandi"

    def get_info(self):
        return f"Admin: {self.ism} {self.familiya}, Login: {self.login}"


# Natija:
# Admin klassi Foydalanuvchi klassidan voris sifatida yaratildi.
# ban_user() metodi foydalanuvchini bloklash haqidagi xabarni qaytardi.
# get_info() metodi admin haqida ma'lumot qaytardi.


# Obyektlar yaratish va metodlarni tekshirish
if __name__ == "__main__":
    talaba1 = Talaba("Ali", "Valiyev", 2)
    fan1 = Fan("Matematika", "Karimov")
    fan2 = Fan("Python", "Rahimov")
    professor1 = Professor("Anvar", "Karimov", 15)
    foydalanuvchi1 = Foydalanuvchi("Hasan", "Aliyev", "hasan01")
    admin1 = Admin("Aziz", "Karimov", "admin01")

    talaba1.fanga_yozil(fan1)
    talaba1.fanga_yozil(fan2)
    talaba1.remove_fan(fan1)

    print("Talabaning fanlari:")
    for fan in talaba1.fanlar:
        print(fan.get_info())

    print(talaba1.get_info())
    print(fan2.get_info())
    print(professor1.get_info())
    print(foydalanuvchi1.get_info())
    print(admin1.ban_user())

    # Natija:
    # Talaba Matematika va Python fanlariga yozildi.
    # Matematika fani ro'yxatdan o'chirildi.
    # Talabaning fanlar ro'yxatida Python fani qoldi.
    # Talabaning fanlari:
    # Fan: Python, O'qituvchi: Rahimov
    # Ismi: Ali, Familiyasi: Valiyev, Bosqichi: 2, Fanlar soni: 1
    # Fan: Python, O'qituvchi: Rahimov
    # Ismi: Anvar, Familiyasi: Karimov, Ish staji: 15
    # Ismi: Hasan, Familiyasi: Aliyev, Login: hasan01
    # Foydalanuvchi bloklandi
