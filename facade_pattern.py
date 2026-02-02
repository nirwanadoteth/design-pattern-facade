"""
Facade Design Pattern Implementation for Mobile Shop
"""

from abc import ABC, abstractmethod


# 1. Interface "MobileShop" dengan metode abstrak "modelNo()" dan "price()"
class MobileShop(ABC):
    """Interface untuk Mobile Shop"""
    
    @abstractmethod
    def modelNo(self):
        """Method abstrak untuk mendapatkan nomor model"""
        pass
    
    @abstractmethod
    def price(self):
        """Method abstrak untuk mendapatkan harga"""
        pass


# 2. Kelas konkret yang mengimplementasikan "MobileShop"
class Asus(MobileShop):
    """Kelas konkret untuk brand Asus"""
    
    def modelNo(self):
        return "Asus ROG Phone 8"
    
    def price(self):
        return 12000000


class Xiaomi(MobileShop):
    """Kelas konkret untuk brand Xiaomi"""
    
    def modelNo(self):
        return "Xiaomi 14 Pro"
    
    def price(self):
        return 9000000


class Samsung(MobileShop):
    """Kelas konkret untuk brand Samsung"""
    
    def modelNo(self):
        return "Samsung Galaxy S24 Ultra"
    
    def price(self):
        return 15000000


# 3. Kelas Facade "ShopKeeper"
class ShopKeeper:
    """Facade class untuk mengelola penjualan berbagai brand mobile"""
    
    def __init__(self):
        # Atribut privat untuk ketiga instansi brand
        self.__asus = Asus()
        self.__xiaomi = Xiaomi()
        self.__samsung = Samsung()
    
    # 4. Metode untuk memanggil metode dari masing-masing brand
    def asusSale(self):
        """Menampilkan informasi penjualan Asus"""
        print(f"Model: {self.__asus.modelNo()}")
        print(f"Harga: Rp {self.__asus.price():,}")
    
    def xiaomiSale(self):
        """Menampilkan informasi penjualan Xiaomi"""
        print(f"Model: {self.__xiaomi.modelNo()}")
        print(f"Harga: Rp {self.__xiaomi.price():,}")
    
    def samsungSale(self):
        """Menampilkan informasi penjualan Samsung"""
        print(f"Model: {self.__samsung.modelNo()}")
        print(f"Harga: Rp {self.__samsung.price():,}")


# 5. Client main untuk tes
def main():
    """Fungsi main untuk testing Facade Pattern"""
    print("=" * 50)
    print("SELAMAT DATANG DI MOBILE SHOP")
    print("=" * 50)
    
    # Membuat instance ShopKeeper (Facade)
    shopkeeper = ShopKeeper()
    
    # Menampilkan informasi penjualan berbagai brand
    print("\n--- Informasi Asus ---")
    shopkeeper.asusSale()
    
    print("\n--- Informasi Xiaomi ---")
    shopkeeper.xiaomiSale()
    
    print("\n--- Informasi Samsung ---")
    shopkeeper.samsungSale()
    
    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
