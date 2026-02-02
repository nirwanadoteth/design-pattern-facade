from typing import override
from MobileShop import MobileShop

class Xiaomi(MobileShop):
    """Kelas konkret untuk brand Xiaomi"""

    @override
    def modelNo(self) -> None:
        print("Model: Xiaomi 14 Pro")

    @override
    def price(self) -> None:
        print("Price: 9000000")
