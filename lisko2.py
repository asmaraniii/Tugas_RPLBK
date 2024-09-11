from abc import ABC, abstractmethod

# Superclass (Abstract)
class Pengiriman(ABC):
    @abstractmethod
    def biaya(self):
        pass

    @abstractmethod
    def estimasi_waktu(self):
        pass

# Subclass 1 (Pengiriman Darat)
class PengirimanDarat(Pengiriman):
    def biaya(self):
        return 50000

    def estimasi_waktu(self):
        return "3 hari"

# Subclass 2 (Pengiriman Laut)
class PengirimanLaut(Pengiriman):
    def biaya(self):
        return 100000

    def estimasi_waktu(self):
        return "7 hari"

# Fungsi yang mengimplementasikan LSP
def hitung_biaya_pengiriman(pengiriman: Pengiriman):
    print(f"Biaya pengiriman: {pengiriman.biaya()} rupiah")
    print(f"Estimasi waktu: {pengiriman.estimasi_waktu()}")

# Menggunakan objek dari kedua subclass
pengiriman_darat = PengirimanDarat()
pengiriman_laut = PengirimanLaut()

# Memanggil fungsi hitung_biaya_pengiriman untuk keduanya
hitung_biaya_pengiriman(pengiriman_darat)
hitung_biaya_pengiriman(pengiriman_laut)
