class Pelanggan:
    def __init__(self, nama, nomor, email):
        self.__nama = nama
        self.__nomor = nomor
        self.__email = email

    def get_nama(self):
        return self.__nama

    def get_nomor(self):
        return self.__nomor

    def get_email(self):
        return self.__email

    def ubah_email(self, email_baru):
        if "@" not in email_baru:
            return False
        self.__email = email_baru
        return True

    def tampilkan_info(self):
        print("Nama Pelanggan :", self.__nama)
        print("Nomor          :", self.__nomor)
        print("Email          :", self.__email)
