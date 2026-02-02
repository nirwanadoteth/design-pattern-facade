from typing import override
from MobileShop import MobileShop

class Asus(MobileShop):
    """Kelas konkret untuk brand Asus"""

    @override
    def modelNo(self) -> None:
        print("Model: Asus ROG Phone 8")

    @override
    def price(self) -> None:
        print("Price: 12000000")
