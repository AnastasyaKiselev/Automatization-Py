from adress import Adress
from mailing import Mailing

from_adress= Adress("197368", "NY", "Pushkina", "kolotushkina", '145')
to_adress = Adress("987456", "SPb", "Shishkina", "Mishkina", '5')

mail1 = Mailing(to_adress, from_adress, 555, "12345678")

print(f"Отправление {mail1.track1} из {mail1.from_adress.index}, {mail1.from_adress.city}, "
      f"{mail1.from_adress.street}, {mail1.from_adress.house}, {mail1.from_adress.apart} в "
      f"{mail1.to_adress.index}, {mail1.to_adress.city}, {mail1.to_adress.street}, {mail1.to_adress.house},"
      f" {mail1.to_adress.apart}. Стоимость {mail1.cost1} рублей." )







# Отправление <track> из <индекс>, <город>, <улица>, <дом> 
#- <квартира> в <индекс>, <город>, <улица>, <дом> -<квартира>. Стоимость <стоимость> рублей.
