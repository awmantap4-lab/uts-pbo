class Pesanan:
    def __init__(self, kode_pesanan, pelanggan):
        self.__kode_pesanan = kode_pesanan
        self.__pelanggan = pelanggan      # relasi ke objek Pelanggan
        self.__items = []                 # relasi ke banyak Menu: [menu, jumlah]
        self.__selesai = False

    def get_kode(self):
        return self.__kode_pesanan

    def get_pelanggan(self):
        return self.__pelanggan

    def is_selesai(self):
        return self.__selesai

    def tambah_item(self, menu, jumlah):
        # Tidak boleh menambah item setelah checkout dan jumlah harus > 0
        if self.__selesai or jumlah <= 0:
            return False
        # Jika menu sudah ada di pesanan, jumlahnya ditambah
        for item in self.__items:
            if item[0] is menu:
                if item[1] + jumlah > menu.get_stok():
                    return False
                item[1] += jumlah
                return True
        # Jika menu belum ada
        if jumlah > menu.get_stok():
            return False
        self.__items.append([menu, jumlah])
        return True

    def hapus_item(self, kode_menu):
        # TODO: hapus item berdasarkan kode menu (return True/False)
        return False

    def get_total(self):
        total = 0
        for menu, jumlah in self.__items:
            total += menu.get_harga() * jumlah
        return total

    def tampilkan_rincian(self):
        print("Pesanan   :", self.__kode_pesanan)
        print("Pelanggan :", self.__pelanggan.get_nama())
        for menu, jumlah in self.__items:
            print(menu.get_nama(), ":", jumlah, "x", menu.get_harga(),
                  "=", menu.get_harga() * jumlah)
        print("TOTAL     :", self.get_total())
        print("Status    :", self.cek_status())

    def cek_status(self):
        return "Lunas" if self.__selesai else "Belum Dibayar"

    def checkout(self):
        # Tidak bisa checkout jika sudah selesai atau belum ada item
        if self.__selesai or not self.__items:
            return False
        # Tahap A: validasi semua stok dulu
        for menu, jumlah in self.__items:
            if jumlah > menu.get_stok():
                return False
        # Tahap B: kurangi stok bila semua valid
        for menu, jumlah in self.__items:
            menu.kurangi_stok(jumlah)
        self.__selesai = True
        return True
