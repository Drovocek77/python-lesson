from smartphone import Smartphone

catalog = []

phone1 = Smartphone("Samsung", "Galaxy S23", "+79123456789")
catalog.append(phone1)

phone2 = Smartphone("Apple", "iPhone 15 Pro", "+79234567890")
catalog.append(phone2)

phone3 = Smartphone("Xiaomi", "Redmi Note 12", "+79345678901")
catalog.append(phone3)

phone4 = Smartphone("Google", "Pixel 8", "+79456789012")
catalog.append(phone4)

phone5 = Smartphone("OnePlus", "11", "+79567890123")
catalog.append(phone5)

print("Каталог телефонов:")
print("-" * 40)

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}.")

print("-" * 40)
print(f"Всего телефонов в каталоге: {len(catalog)}")
