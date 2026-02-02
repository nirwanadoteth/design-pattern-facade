from Asus import Asus
from Xiaomi import Xiaomi
from Samsung import Samsung

class ShopKeeper:
    """Facade class untuk mengelola penjualan berbagai brand mobile"""

    def __init__(self):
        self.__asus = Asus()
        self.__xiaomi = Xiaomi()
        self.__samsung = Samsung()

    def asusSale(self):
        """Menampilkan informasi penjualan Asus"""
        self.__asus.modelNo()
        self.__asus.price()

    def xiaomiSale(self):
        """Menampilkan informasi penjualan Xiaomi"""
        self.__xiaomi.modelNo()
        self.__xiaomi.price()

    def samsungSale(self):
        """Menampilkan informasi penjualan Samsung"""
        self.__samsung.modelNo()
        self.__samsung.price()
