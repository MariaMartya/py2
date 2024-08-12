def month_to_season(month_number):
    if month_number == 12 or month_number <= 2:
        print("Зима")
    elif month_number >= 3 and month_number <= 5:
        print("Весна")
    elif month_number >= 6 and month_number <= 8:
        print("Лето")
    elif month_number >= 9 and month_number <= 11:
        print("Осень")
    elif month_number < 1 or month_number > 12:
      print("Неверный номер месяца")
 

month_number=12
month_to_season(month_number)