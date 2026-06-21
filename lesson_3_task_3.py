from address import Address
from mailing import Mailing

to_addr = Address("190000", "Санкт-Петербург", "Невский пр.", "10", "25")
from_addr = Address("101000", "Москва", "Тверская ул.", "5", "12")

shipment = Mailing(to_addr, from_addr, 450, "TRACK1234567")

print(
    f"Отправление {shipment.track} из {shipment.from_address.index}, "
    f"{shipment.from_address.city}, {shipment.from_address.street}, "
    f"{shipment.from_address.house} - {shipment.from_address.apartment} в "
    f"{shipment.to_address.index}, {shipment.to_address.city}, "
    f"{shipment.to_address.street}, {shipment.to_address.house} - "
    f"{shipment.to_address.apartment}. Стоимость {shipment.cost} рублей."
)
