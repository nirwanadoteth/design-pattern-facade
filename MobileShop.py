from abc import ABC, abstractmethod


class MobileShop(ABC):
    """Interface untuk Mobile Shop"""

    @abstractmethod
    def modelNo(self):
        """Method abstrak untuk mendapatkan nomor model"""

    @abstractmethod
    def price(self):
        """Method abstrak untuk mendapatkan harga"""
