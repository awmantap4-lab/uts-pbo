from menu import Menu

class Makanan(Menu):
    def __init__(self, kode, nama, harga, stok, porsi, tingkat_pedas, jenis):
        super().__init__(kode, nama, harga, stok)   # panggil constructor superclass
        if tingkat_pedas < 0 or tingkat_pedas > 5:
            raise ValueError("tingkat pedas harus 0 - 5")
        if jenis not in ("Utama", "Pembuka", "Penutup"):
            raise ValueError("jenis harus Utama / Pembuka / Penutup")
        self.__porsi = porsi
        self.__tingkat_pedas = tingkat_pedas
        self.__jenis = jenis          # Utama / Pembuka / Penutup

    def get_porsi(self):
        return self.__porsi

    def get_tingkat_pedas(self):
        return self.__tingkat_pedas

    def get_jenis(self):
        return self.__jenis

    def info_makanan(self):
        return f"Porsi: {self.__porsi}, Pedas: {self.__tingkat_pedas}, Jenis: {self.__jenis}"

    # Override method superclass
    def get_kategori(self):
        return "Makanan"

    def tampilkan_info(self):
        super().tampilkan_info()
        print("Detail   :", self.info_makanan())
