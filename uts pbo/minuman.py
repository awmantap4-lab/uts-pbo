from menu import Menu

class Minuman(Menu):
    def __init__(self, kode, nama, harga, stok, ukuran, suhu, kadar_gula):
        super().__init__(kode, nama, harga, stok)
        if ukuran.upper() not in ("S", "M", "L"):
            raise ValueError("ukuran harus S / M / L")
        if suhu not in ("Panas", "Dingin"):
            raise ValueError("suhu harus Panas / Dingin")
        if kadar_gula not in ("Normal", "Less Sugar"):
            raise ValueError("kadar gula harus Normal / Less Sugar")
        self.__ukuran = ukuran.upper()
        self.__suhu = suhu                # Panas / Dingin
        self.__kadar_gula = kadar_gula    # Normal / Less Sugar

    def get_ukuran(self):
        return self.__ukuran

    def get_suhu(self):
        return self.__suhu

    def get_kadar_gula(self):
        return self.__kadar_gula

    def info_minuman(self):
        return f"Ukuran: {self.__ukuran}, Suhu: {self.__suhu}, Gula: {self.__kadar_gula}"

    def get_kategori(self):
        return "Minuman"

    def tampilkan_info(self):
        super().tampilkan_info()
        print("Detail   :", self.info_minuman())
