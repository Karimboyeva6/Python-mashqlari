import unittest


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


# ============================================
#              UNITTESTLAR
# ============================================

class TestShaxsvaTalaba(unittest.TestCase):
    def setUp(self):
        self.talaba1 = Talaba("Yulduz", "Karimboyeva", "AA1234567", 2, "T001")
        self.talaba2 = Talaba("Ali", "Valiyev", "AB7654321", 3, "T002")

    def test_isinstance_tekshiruv(self):
        self.assertIsInstance(self.talaba2, Talaba)
        self.assertIsInstance(self.talaba1, Shaxs)

    def test_get_info(self):
        self.assertEqual(
            self.talaba1.get_info(),
            "Ismi: Yulduz, Familiyasi: Karimboyeva, Bosqichi: 2, Fanlar soni: 0"
        )
        self.assertEqual(
            self.talaba2.get_info(),
            "Ismi: Ali, Familiyasi: Valiyev, Bosqichi: 3, Fanlar soni: 0"
        )

    def test_fanga_yozil(self):
        self.assertEqual(self.talaba1.fanlar, [])
        self.talaba2.fanga_yozil("Python dasturlash tili")
        self.assertEqual(self.talaba2.fanlar, ["Python dasturlash tili"])


if __name__ == "__main__":
    unittest.main()


# ============================================
#   TERMINALDA "python3 shaxs_talaba.py -v"
#   BUYRUG'INI ISHGA TUSHIRGANDAGI NATIJA:
# ============================================
#
# test_fanga_yozil (__main__.TestShaxsvaTalaba.test_fanga_yozil) ... ok
# test_get_info (__main__.TestShaxsvaTalaba.test_get_info) ... ok
# test_isinstance_tekshiruv (__main__.TestShaxsvaTalaba.test_isinstance_tekshiruv) ... ok
#
# ----------------------------------------------------------------------
# Ran 3 tests in 0.005s
#
# OK
#
# ============================================
# Xulosa: barcha 3 ta test muvaffaqiyatli o'tdi (OK).
# - test_isinstance_tekshiruv -> Talaba obyekti ham Talaba, ham Shaxs
#   turiga tegishli ekanligini tasdiqladi (meros to'g'ri ishlaydi)
# - test_get_info -> get_info() metodi ikkala klass obyekti uchun ham
#   kutilgan matnni to'g'ri qaytardi
# - test_fanga_yozil -> fanga_yozil() metodi chaqirilgach, fanlar
#   ro'yxati to'g'ri yangilanganini tasdiqladi
