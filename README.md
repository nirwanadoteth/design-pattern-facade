# Design Pattern: Facade

Implementasi Facade Pattern dalam Python untuk sistem penjualan mobile phone.

## Deskripsi

Facade Pattern adalah design pattern struktural yang menyediakan interface sederhana untuk sistem yang kompleks. Dalam contoh ini, `ShopKeeper` bertindak sebagai facade yang menyederhanakan akses ke berbagai brand mobile phone.

## Struktur

1. **Interface `MobileShop`**: Interface abstrak dengan metode `modelNo()` dan `price()`
2. **Kelas Konkret**:
   - `Asus`: Implementasi untuk brand Asus
   - `Xiaomi`: Implementasi untuk brand Xiaomi
   - `Samsung`: Implementasi untuk brand Samsung
3. **Facade `ShopKeeper`**: Menyederhanakan akses ke berbagai brand dengan menyediakan metode:
   - `asusSale()`
   - `xiaomiSale()`
   - `samsungSale()`

## Cara Menjalankan

```bash
python3 FacadePatternClient.py
```

## Output

```md
==================================================
SELAMAT DATANG DI MOBILE SHOP
==================================================

--- Informasi Asus ---
Model: Asus ROG Phone 8
Harga: Rp 12,000,000

--- Informasi Xiaomi ---
Model: Xiaomi 14 Pro
Harga: Rp 9,000,000

--- Informasi Samsung ---
Model: Samsung Galaxy S24 Ultra
Harga: Rp 15,000,000

==================================================
```

## Manfaat Facade Pattern

- Menyederhanakan interface kompleks
- Mengurangi ketergantungan client terhadap subsistem
- Memudahkan penggunaan sistem
- Meningkatkan maintainability code
