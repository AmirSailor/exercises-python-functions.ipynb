def count_sundays():
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_of_week = 1  # 1 Jan 1900 was a Monday (0=Sunday, 1=Monday, etc.)
    sunday_count = 0

    # Advance to 1 Jan 1901
    for year in range(1900, 1901):
        for month in range(12):
            if month == 1 and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
                day_of_week += 29
            else:
                day_of_week += days_in_month[month]
            day_of_week %= 7  # Keep it in [0,6] range

    # Count Sundays from 1901 to 2000
    for year in range(1901, 2001):
        for month in range(12):
            if day_of_week == 0:  # 0 = Sunday
                sunday_count += 1

            # Move to the next month
            if month == 1 and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
                day_of_week += 29
            else:
                day_of_week += days_in_month[month]

            day_of_week %= 7  # Keep it in [0,6] range

    return sunday_count

print(count_sundays())
