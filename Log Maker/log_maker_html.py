from datetime import date
from calendar import monthrange
from inflect import engine

def make_logs(month, year):
    this_month = date(year, month, 1).strftime('%B')
    number_of_days = max(list(monthrange(year, month)))
    p = engine()
    with open(this_month + '_' + str(year) + '.html', 'w') as f:
        f.write(
            f"<p><strong>CP's Logs ({this_month} {year})\n______________________________________________________________________________\n</strong></p>")
        for day in range(1, number_of_days + 1):
            weekday = date(year, month, day).strftime('%A')
            f.write(
                f'<p><strong>{weekday}, {this_month} {p.ordinal(day)}, {year}<br><br></strong></p>')
            f.write('<p><strong>END LOG\n')
            f.write('______________________________________________________________________________\n</strong></p>')

make_logs(1, 2021)
