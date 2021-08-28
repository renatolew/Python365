# Write a Python program to calculate number of days between two dates.

date1_year = int(input('Type the year of the first date: '))
date1_month = int(input('Type the month of the first date: '))
date1_day = int(input('Type the day of the first date: '))
date2_year = int(input('Type the year of the second date: '))
date2_month = int(input('Type the month of the second date: '))
date2_day = int(input('Type the date of the second date: '))




def days_in_date(year, month, day):
    calc = 365 * year + 12 * month + day
    return calc


date1_calc = days_in_date(date1_year, date1_month, date1_day)
date2_calc = days_in_date(date2_year, date2_month, date2_day)
date_dif = abs(date1_calc - date2_calc)

print('The difference in days between {}/{}/{} and {}/{}/{} is {} days.'.format(date1_day, date1_month, date1_year, date2_day, date2_month, date2_year, date_dif))