def is_year_leap(year):
       if year%4 == 0:
            return (True)
       else:   return (False)

a = 2000       
is_year_leap(a)
b = is_year_leap(a)
print("год", a, "|", b)

 #year=int(input("Введите год"))