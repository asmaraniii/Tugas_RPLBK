from abc import ABC, abstractmethod

# Superclass (Abstract)
class Avenger(ABC):
    @abstractmethod
    def serang(self):
        pass

    @abstractmethod
    def bertahan(self):
        pass

# Subclass 1 (Iron Man)
class IronMan(Avenger):
    def serang(self):
        return "Iron Man menembakkan repulsor dari armornya!"

    def bertahan(self):
        return "Iron Man menggunakan perisai energi dari armornya!"

    def teknologi_stark(self):
        return "Iron Man mengakses teknologi Stark yang canggih."

# Subclass 2 (Captain America)
class CaptainAmerica(Avenger):
    def serang(self):
        return "Captain America melempar perisainya dengan akurasi tinggi!"

    def bertahan(self):
        return "Captain America bertahan menggunakan perisai vibraniumnya!"

    def strategi_tempur(self):
        return "Captain America mengatur strategi tempur yang brilian."

# Subclass 3 (Thor)
class Thor(Avenger):
    def serang(self):
        return "Thor menghantam musuh dengan Mjolnir dan petir Asgard!"

    def bertahan(self):
        return "Thor menggunakan kekuatan ilahi dan Mjolnir untuk bertahan!"

    def kekuatan_asgard(self):
        return "Thor memanggil kekuatan Asgard dan petir untuk memperkuat serangannya."

# Fungsi yang mengimplementasikan LSP
def aksi_avenger(avenger: Avenger):
    print(f"{type(avenger).__name__}:")
    print(avenger.serang())
    print(avenger.bertahan())
    print()

# Menggunakan objek dari subclass Avengers
iron_man = IronMan()
captain_america = CaptainAmerica()
thor = Thor()

# Memanggil fungsi aksi_avenger untuk masing-masing Avenger
aksi_avenger(iron_man)
aksi_avenger(captain_america)
aksi_avenger(thor)
