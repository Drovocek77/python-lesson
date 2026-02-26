from address import Address
from mailing import Mailing

from_address = Address("123456", "Москва", "Тверская", "15", "42")
to_address = Address("654321", "Санкт-Петербург", "Невский", "28", "15")

mailing = Mailing(to_address, from_address, 350.50, "AB123456789RU")

print(f"Отправление {mailing.track} "
      f"из {mailing.from_address.get_full_address()} "
      f"в {mailing.to_address.get_full_address()}. "
      f"Стоимость {mailing.cost} рублей.")
