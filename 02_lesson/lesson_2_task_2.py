def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


current_year = 2024
result = is_year_leap(current_year)

print(f"год {current_year}: {result}")
