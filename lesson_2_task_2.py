def is_year_leap(year):
    if (year % 4 == 0 ):
        return True
    else:
        return False

year = (input("Проверим год :"))
year=int(year)
x=is_year_leap(year)
print("Год ", year , is_year_leap(year))