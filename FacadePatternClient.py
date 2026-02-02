"""
Facade Design Pattern Implementation untuk Mobile Shop
"""

from ShopKeeper import ShopKeeper

class FacadePatternClient:
    """Client main untuk tes Facade Pattern"""
    @staticmethod
    def main():
        """Fungsi main untuk testing Facade Pattern"""
        print("=" * 50)
        print("SELAMAT DATANG DI MOBILE SHOP")
        print("=" * 50)

        shopkeeper = ShopKeeper()

        print("\n--- Informasi Asus ---")
        shopkeeper.asusSale()

        print("\n--- Informasi Xiaomi ---")
        shopkeeper.xiaomiSale()

        print("\n--- Informasi Samsung ---")
        shopkeeper.samsungSale()

        print("\n" + "=" * 50)



if __name__ == "__main__":
    FacadePatternClient.main()
