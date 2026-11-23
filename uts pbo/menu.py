# ============================================================
# menu.py - SUPERCLASS
# ============================================================
class Menu:
    # Constructor berparameter + validasi
    def __init__(self, kode="", nama="", harga=0, stok=0):
        if harga < 0 or stok < 0:
            raise ValueError("harga/stok tidak valid")
        # Atribut private (enkapsulasi)
        self.__kode = kode
        self.__nama = nama
        self.__harga = harga
        self.__stok = stok

    # ---------- Getter ----------
    def get_kode(self):
        return self.__kode

    def get_nama(self):
        return self.__nama

    def get_harga(self):
        return self.__harga

    def get_stok(self):
        return self.__stok

    # ---------- Method tambahan ----------
    def ubah_harga(self, harga_baru):
        # Mengubah harga lewat method (bukan langsung ke atribut)
        if harga_baru < 0:
            return False
        self.__harga = harga_baru
        return True

    def ubah_nama(self, nama_baru):
        if nama_baru.strip() == "":
            return False
        self.__nama = nama_baru
        return True

    def tambah_stok(self, jumlah):
        if jumlah <= 0:
            raise ValueError("Jumlah penambahan stok harus lebih dari 0.")
        self.__stok += jumlah

    def kurangi_stok(self, jumlah):
        if jumlah <= 0:
            raise ValueError("Jumlah pengurangan stok harus lebih dari 0.")
        if jumlah > self.__stok:
            raise ValueError("Stok tidak mencukupi.")
        self.__stok -= jumlah

    def get_kategori(self):
        # Akan di-override oleh subclass
        return "Menu"

    def cek_status(self):
        # Status data menu: Tersedia bila stok masih ada
        return "Tersedia" if self.__stok > 0 else "Habis"

    def tampilkan_info(self):
        print("Kode     :", self.__kode)
        print("Nama     :", self.__nama)
        print("Kategori :", self.get_kategori())
        print("Harga    :", self.__harga)
        print("Stok     :", self.__stok, f"({self.cek_status()})")
