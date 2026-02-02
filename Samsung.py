from typing import override
from MobileShop import MobileShop

class Samsung(MobileShop):
    """Kelas konkret untuk brand Samsung"""

    @override
    def modelNo(self) -> None:
        print("Model: Samsung Galaxy S24 Ultra")

    @override
    def price(self) -> None:
        print("Price: 15000000")
