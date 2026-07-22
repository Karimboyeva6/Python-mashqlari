
# 1-TOPSHIRIQ: Uchta sondan eng kattasini topish


def max_son(a, b, c):
    son = max(a, b, c)
    return son


# --- Test ---
import unittest


class Test_max(unittest.TestCase):
    def test_oddiyholat(self):
        self.assertEqual(max_son(2, 5, 8), 8)

    def test_teng(self):
        self.assertEqual(max_son(5, 5, 5), 5)

    def test_manfiy(self):
        self.assertEqual(max_son(-2, -3, -6), -2)

    def test_ikkitasiteng(self):
        self.assertEqual(max_son(5, 3, 5), 5)


# Natija:

# Ran 4 tests in 0.003s
#
# OK


# 2-TOPSHIRIQ: Ro'yxatdagi matnlarning birinchi harfini katta qilish

def matn_title(royxat):
    yangi_royxat = []
    for matn in royxat:
        x = matn.title()
        yangi_royxat.append(x)
    return yangi_royxat


# --- Test ---
class Test_title(unittest.TestCase):
    def test_matn_title(self):
        self.assertListEqual(matn_title(["apple", "banana", "cherry"]), ["Apple", "Banana", "Cherry"])

    def test_bosh(self):
        self.assertListEqual(matn_title([]), [])

    def test_bitta_matn(self):
        self.assertListEqual(matn_title(["hello"]), ["Hello"])


# Natija:
# ...

# Ran 3 tests in 0.003s
#
# OK



# 3-TOPSHIRIQ: Ro'yxatdan juft sonlarni ajratib olish
# 

def juft_son_ajrat(royxat):
    yangi_royxat = []
    for x in royxat:
        if x % 2 == 0:
            yangi_royxat.append(x)
    return yangi_royxat


# --- Test ---
class Test_juftmi(unittest.TestCase):
    def testbarchasi_juft(self):
        self.assertListEqual(juft_son_ajrat([2, 4, 6]), [2, 4, 6])

    def test_aralash(self):
        self.assertListEqual(juft_son_ajrat([5, 9, 6]), [6])

    def test_manfiy(self):
        self.assertListEqual(juft_son_ajrat([-2, -1, -4]), [-2, -4])


# Natija:
# 
# Ran 3 tests in 0.003s
#
# OK


# 
# 4-TOPSHIRIQ: Son Fibonachchi ketma-ketligida bormi
#

def fibonachchimi(son):
    a, b = 0, 1
    while a < son:
        a, b = b, a + b
    return a == son


# --- Test ---
class Test_fibon(unittest.TestCase):
    def test_True(self):
        self.assertTrue(fibonachchimi(2))

    def test_False(self):
        self.assertFalse(fibonachchimi(4))


# Natija:
# 
# Ran 2 tests in 0.001s
#
# OK



# BARCHA TESTLARNI ISHGA TUSHIRISH

if __name__ == '__main__':
    unittest.main()
