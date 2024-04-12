def month_to_season(month_number):
        if month_number == 1 or  (month_number == 2) or (month_number == 12):
                return ("Зима")
        elif month_number == 3 or  (month_number == 4) or (month_number == 5):
                return ("Весна")
        elif month_number == 6 or  (month_number == 7) or (month_number == 8):
                return ("Лето")
        elif month_number == 9 or  (month_number == 10) or (month_number == 11):
                return ("Осень")
        else: return ("Нет такого месяца")

a = 1
b = month_to_season(a)
print (b) 