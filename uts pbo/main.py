from makanan import Makanan
from minuman import Minuman
from pelanggan import Pelanggan
from pesanan import Pesanan

daftar_menu = []
daftar_pesanan = []


def data_awal():
    """Data contoh agar program tidak kosong saat pertama dijalankan."""
    daftar_menu.append(Makanan("M01", "Nasi Goreng", 20000, 10, "Besar", 3, "Utama"))
    daftar_menu.append(Minuman("M02", "Es Teh", 5000, 20, "M", "Dingin", "Normal"))


def input_angka(teks):
    """Input angka yang aman dari error."""
    while True:
        try:
            return int(input(teks))
        except ValueError:
            print("Masukkan angka yang valid!")


def cari_menu(kode):
    for m in daftar_menu:
        if m.get_kode().lower() == kode.lower():
            return m
    return None


def cari_pesanan(kode):
    for p in daftar_pesanan:
        if p.get_kode().lower() == kode.lower():
            return p
    return None

# ---------- 1. Tampilkan data ----------
def tampilkan_data():
    print("\n--- DAFTAR MENU ---")
    for m in daftar_menu:
        m.tampilkan_info()
        print("-" * 15)
    print("\n--- DAFTAR PESANAN ---")
    # TODO: tampilkan semua pesanan memakai p.tampilkan_rincian()


# ---------- 2. Cari data ----------
def cari_data():
    print("\n--- CARI MENU ---")
    # TODO: cari juga berdasarkan nama (sebagian kata)
    m = cari_menu(input("Kode menu: "))
    if m:
        m.tampilkan_info()
    else:
        print("Data tidak ditemukan.")


# ---------- 3. Ubah data ----------
def ubah_data():
    print("\n--- UBAH DATA MENU ---")
    m = cari_menu(input("Kode menu: "))
    if m is None:
        print("Data tidak ditemukan.")
        return
    harga_baru = input_angka("Harga baru: ")
    print("Harga diubah." if m.ubah_harga(harga_baru) else "Harga tidak valid.")
    # TODO: tambahkan ubah nama (ubah_nama) dan tambah stok (tambah_stok)


# ---------- 4. Cek status data ----------
def cek_status():
    print("\n--- CEK STATUS ---")
    print("1. Status menu   2. Status pesanan")
    pilih = input("Pilih: ")
    if pilih == "1":
        for m in daftar_menu:
            print(m.get_kode(), m.get_nama(), "->", m.cek_status())
    elif pilih == "2":
        p = cari_pesanan(input("Kode pesanan: "))
        if p is None:
            print("Pesanan tidak ditemukan.")
            return
        p.tampilkan_rincian()
        if not p.is_selesai() and input("Checkout sekarang? (y/n): ").lower() == "y":
            print("Checkout berhasil." if p.checkout() else "Checkout gagal.")

            # ---------- 5. Tambah data ----------
def tambah_data():
    print("\n--- TAMBAH DATA ---")
    print("1. Menu baru   2. Pesanan baru   3. Tambah item ke pesanan")
    pilih = input("Pilih: ")

    if pilih == "1":
        jenis = input("Jenis (1=Makanan, 2=Minuman): ")
        kode = input("Kode : ")
        if cari_menu(kode):
            print("Kode sudah dipakai!")
            return
        nama = input("Nama : ")
        harga = input_angka("Harga: ")
        stok = input_angka("Stok : ")
        try:   # constructor bisa raise ValueError
            if jenis == "1":
                porsi = input("Porsi (Kecil/Besar): ")
                pedas = input_angka("Tingkat pedas (0-5): ")
                jns = input("Jenis (Utama/Pembuka/Penutup): ")
                daftar_menu.append(Makanan(kode, nama, harga, stok, porsi, pedas, jns))
            else:
                ukuran = input("Ukuran (S/M/L): ")
                suhu = input("Suhu (Panas/Dingin): ")
                gula = input("Kadar gula (Normal/Less Sugar): ")
                daftar_menu.append(Minuman(kode, nama, harga, stok, ukuran, suhu, gula))
            print("Menu berhasil ditambahkan.")
        except ValueError as e:
            print("Gagal:", e)

    elif pilih == "2":
        kode = input("Kode pesanan : ")
        if cari_pesanan(kode):
            print("Kode sudah dipakai!")
            return
        pelanggan = Pelanggan(input("Nama pelanggan : "),
                              input("Nomor pelanggan: "),
                              input("Email pelanggan: "))
        daftar_pesanan.append(Pesanan(kode, pelanggan))
        print("Pesanan berhasil dibuat.")

    elif pilih == "3":
        p = cari_pesanan(input("Kode pesanan: "))
        m = cari_menu(input("Kode menu   : "))
        if p is None or m is None:
            print("Pesanan / menu tidak ditemukan.")
            return
        jumlah = input_angka("Jumlah: ")
        print("Berhasil." if p.tambah_item(m, jumlah) else "Gagal (stok kurang / pesanan selesai).")


def main():
    data_awal()
    while True:
        print("\n===== KASIR RESTORAN =====")
        print("1. Tampilkan Data")
        print("2. Cari Data")
        print("3. Ubah Data")
        print("4. Cek Status Data")
        print("5. Tambah Data")
        print("0. Keluar")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            tampilkan_data()
        elif pilihan == "2":
            cari_data()
        elif pilihan == "3":
            ubah_data()
        elif pilihan == "4":
            cek_status()
        elif pilihan == "5":
            tambah_data()
        elif pilihan == "0":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
