from datetime import date
from calendar import monthrange
from inflect import engine

def make_logs(month, year):
    this_month = date(year, month, 1).strftime('%B')
    number_of_days = max(list(monthrange(year, month)))
    p = engine()
    with open(this_month + '_' + str(year) + '.txt', 'w') as f:
        f.write(f"CP's Logs ({this_month} {year})" )
        for day in range(1, number_of_days + 1):
            weekday = date(year, month, day).strftime('%A')
            f.write(f'{weekday}, {this_month} {p.ordinal(day)}, {year}\n\n\n\n')
            f.write('END LOG\n')
            f.write('______________________________________________________________________________\n\n')

make_logs(1, 2021)
