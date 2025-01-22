class Hotel:
    def __init__(self, nama, jumlah_kamar):
        self.nama = nama
        self.jumlah_kamar = jumlah_kamar
        self.kamar_terisi = 0
        self.reservasi = {}

    def tampilkan_info(self):
        print(f"\n--- Info Hotel {self.nama} ---")
        print(f"Total kamar: {self.jumlah_kamar}")
        print(f"Kamar yang terisi: {self.kamar_terisi}")
        print(f"Kamar yang tersedia: {self.jumlah_kamar - self.kamar_terisi}")

    def reservasi_kamar(self, nama_pelanggan, jumlah_kamar):
        if self.kamar_terisi + jumlah_kamar <= self.jumlah_kamar:
            self.kamar_terisi += jumlah_kamar
            self.reservasi[nama_pelanggan] = jumlah_kamar
            print(f"Reservasi berhasil untuk {nama_pelanggan} dengan {jumlah_kamar} kamar.")
        else:
            print("Maaf, kamar tidak cukup tersedia.")

    def batal_reservasi(self, nama_pelanggan):
        if nama_pelanggan in self.reservasi:
            jumlah_kamar = self.reservasi.pop(nama_pelanggan)
            self.kamar_terisi -= jumlah_kamar
            print(f"Reservasi atas nama {nama_pelanggan} telah dibatalkan.")
        else:
            print("Reservasi tidak ditemukan.")

def menu_reservasi():
    hotel = Hotel("Hotel Sejahtera", 10)

    while True:
        print("\n--- Menu Reservasi Hotel ---")
        print("1. Tampilkan Info Hotel")
        print("2. Lakukan Reservasi")
        print("3. Batalkan Reservasi")
        print("4. Keluar")
        pilihan = input("Pilih menu (1/2/3/4): ")

        if pilihan == '1':
            hotel.tampilkan_info()
        elif pilihan == '2':
            nama_pelanggan = input("Nama Pelanggan: ")
            jumlah_kamar = int(input("Jumlah Kamar yang diinginkan: "))
            hotel.reservasi_kamar(nama_pelanggan, jumlah_kamar)
        elif pilihan == '3':
            nama_pelanggan = input("Nama Pelanggan: ")
            hotel.batal_reservasi(nama_pelanggan)
        elif pilihan == '4':
            print("Terima kasih telah menggunakan layanan reservasi.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    menu_reservasi()
