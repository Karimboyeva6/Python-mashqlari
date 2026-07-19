1#
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

    def __repr__(self):
        return f"Shaxs: {self.ism}, {self.familiya}"


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
        return (f"Ismi: {self.ism}, Familiyasi: {self.familiya}, "
                f"Bosqichi: {self.bosqich}, Fanlar soni: {len(self.fanlar)}")

    def get_id_raqam(self):
        return f"Foydalanuvchining ID raqami: {self.__id_raqam}"

    def set_id_raqam(self, yangi_id):
        self.__id_raqam = yangi_id

    @classmethod
    def get_talabalar_soni(cls):
        return cls.talabalar_soni

    def __repr__(self):
        return f"Talaba: {self.ism}, {self.familiya}, {self.bosqich} bosqich"

    def __eq__(self, boshqa):
        return self.bosqich == boshqa.bosqich

    def __lt__(self, boshqa):
        return self.bosqich < boshqa.bosqich

if __name__ == "__main__":
    talaba1 = Talaba("Yulduz", "Karimboyeva", "AA1234567", 2, "T001")
    talaba2 = Talaba("Ali", "Valiyev", "AB7654321", 3, "T002")

    print(talaba1.get_info())
    # Natija: Ismi: Yulduz, Familiyasi: Karimboyeva, Bosqichi: 2, Fanlar soni: 0

    print(talaba1.get_passport())
    # Natija: Foydalanuvchining passporti: AA1234567

    print(talaba1.get_id_raqam())
    # Natija: Foydalanuvchining ID raqami: T001

    talaba1.fanga_yozil("Python dasturlash")
    talaba1.fanga_yozil("Matematika")
    print(talaba1.get_info())
    # Natija: ... Fanlar soni: 2

    print(talaba1)
    # Natija: Talaba: Yulduz, Karimboyeva, 2 bosqich

    print(talaba1 == talaba2)
    # Natija: False (2-bosqich != 3-bosqich)

    print(talaba1 < talaba2)
    # Natija: True (2 < 3)

    print("Jami talabalar soni:", Talaba.get_talabalar_soni())
    # Natija: Jami talabalar soni: 2

    print("Jami shaxslar soni:", Shaxs.get_odamlar_soni())
    # Natija: Jami shaxslar soni: 2


2#
class Fan:
    """Fan obyekti: nomi va shu fanga yozilgan talabalar ro'yxatini saqlaydi"""

    def __init__(self, nomi):
        self.nomi = nomi
        self.talabalar = []

    def add_student(self, talaba):
        """Fanga talaba qo'shish"""
        self.talabalar.append(talaba)

    def __getitem__(self, index):
        """fan[0] kabi indeks orqali talabani olish"""
        return self.talabalar[index]

    def __setitem__(self, index, talaba):
        """fan[0] = yangi_talaba kabi mavjud talabani almashtirish"""
        self.talabalar[index] = talaba

    def __len__(self):
        """len(fan) - fanga yozilgan talabalar sonini qaytaradi"""
        return len(self.talabalar)

    def __add__(self, talaba):
        """fan + talaba -> talabani fanga qo'shadi"""
        self.add_student(talaba)
        return self

    def __sub__(self, passport_id):
        """fan - passport_id -> shu ID'ga ega talabani fandan olib tashlaydi"""
        for talaba in self.talabalar:
            if talaba.passport_id == passport_id:
                self.talabalar.remove(talaba)
                break
        return self

    def __call__(self, talaba=None):
        """
        fan() -> fanga yozilgan barcha talabalarni chiqaradi
        fan(talaba) -> shu talaba fanda bor-yo'qligini tekshiradi
        """
        if talaba is None:
            print(f"'{self.nomi}' faniga yozilgan talabalar:")
            for t in self.talabalar:
                print(" -", t)
            return self.talabalar
        else:
            if talaba in self.talabalar:
                print(f"{talaba.ism} '{self.nomi}' fanida bor.")
                return True
            else:
                print(f"{talaba.ism} '{self.nomi}' fanida yo'q.")
                return False

if __name__ == "__main__":
    # Fan obyekti yaratamiz
    python = Fan("Python dasturlash")

   
    talaba1 = Talaba("Yulduz Karimboyeva", "AA1234567")  # <-- siz shu yerdasiz
    talaba2 = Talaba("Ali Valiyev", "AB7654321")

    # + operatori orqali talaba qo'shish
    python + talaba1
    python + talaba2
    # Natija: talaba1 va talaba2 python.talabalar ro'yxatiga qo'shildi

    # __len__ - talabalar sonini ko'rish
    print(len(python))
    # Natija: 2

    # __getitem__ - indeks orqali talabani olish
    print(python[0])
    # Natija: Talaba(Yulduz Karimboyeva, ID: AA1234567)

    # __setitem__ - indeks orqali talabani almashtirish
    talaba3 = Talaba("Sardor Nomozov", "AC1112223")
    python[1] = talaba3
    print(python[1])
    # Natija: Talaba(Sardor Nomozov, ID: AC1112223)

    # __call__ - argumentsiz chaqirish -> barcha talabalarni chiqaradi
    python()
    # Natija:
    # 'Python dasturlash' faniga yozilgan talabalar:
    #  - Talaba(Yulduz Karimboyeva, ID: AA1234567)
    #  - Talaba(Sardor Nomozov, ID: AC1112223)

    # __call__ - talaba bilan chaqirish -> mavjudligini tekshiradi
    python(talaba1)
    # Natija: Yulduz Karimboyeva 'Python dasturlash' fanida bor.

    # - operatori orqali talabani ID bo'yicha olib tashlash
    python - "AA1234567"
    # Natija: Yulduz Karimboyeva ro'yxatdan olib tashlanadi

    python()
    # Natija:
    # 'Python dasturlash' faniga yozilgan talabalar:
    #  - Talaba(Sardor Nomozov, ID: AC1112223)