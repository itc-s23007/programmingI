def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_month_days(year, month):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year) and month == 2:
        return 29
    return days_in_month[month - 1]

def print_calendar(year, month):
    month_names = [
        "", "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    
    month_name = month_names[month]
    num_days = get_month_days(year, month)
    
    print(f"     {month_name} {year}")
    print("日 月 火 水 木 金 土")
    
    first_day_of_month = 1  # Assume the first day is Sunday
    for day in range(1, num_days + 1):
        if day == 1:
            first_day_of_month = (first_day_of_month + 6) % 7  # Calculate the actual first day
            print(" " * 3 * first_day_of_month, end="")
        
        print(f"{day:2d}", end=" ")
        
        if (day + first_day_of_month) % 7 == 0:
            print()
    
    print()

year = 2023
month = 8
print_calendar(year, month)

