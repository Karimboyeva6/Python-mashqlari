class User:
    def init(self, foydalanuvchi_ismi, ism, email):
        self.foydalanuvchi_ismi = foydalanuvchi_ismi
        self.ism = ism
        self.email = email

    def get_info(self):
        return f"Foydalanuvchi: {self.foydalanuvchi_ismi}, Ismi: {self.ism}, Email: {self.email}"

u1 = User("yulduz2005", "Yulduz Karimboyeva", "yulduz2005@gmail.com")
u2 = User("munisa0099", "Munisa Abdullayeva", "munisa0099@gmail.com")
u3 = User("guli7689", "Gulnoza Sharipova", "guli7689@gmail.com")
u4 = User("anvar5467", "Anvar Mirahmedov", "anvar5467@gmail.com")

print(u1.get_info())
print(u2.get_info())
print(u3.get_info())
print(u4.get_info())

print(u1.foydalanuvchi_ismi)
print(u2.ism)
print(u4.email)

# Natija:
# Foydalanuvchi: yulduz2005, Ismi: Yulduz Karimboyeva, Email: yulduz2005@gmail.com
# Foydalanuvchi: munisa0099, Ismi: Munisa Abdullayeva, Email: munisa0099@gmail.com
# Foydalanuvchi: guli7689, Ismi: Gulnoza Sharipova, Email: guli7689@gmail.com
# Foydalanuvchi: anvar5467, Ismi: Anvar Mirahmedov, Email: anvar5467@gmail.com
# yulduz2005
# Munisa Abdullayeva
# anvar5467@gmail.com