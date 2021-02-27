from datetime import date
from calendar import monthrange
from inflect import engine

def make_logs(month, year):
    this_month = date(year, month, 1).strftime('%B')
    number_of_days = max(list(monthrange(year, month)))
    p = engine()
    with open(this_month + '_' + str(year) + '.html', 'w') as f:
        f.write(
            f"<p><strong>CP's Logs ({this_month} {year})<br>\n____________________________________________________________________________\n</strong><br><br>")
        for day in range(1, number_of_days + 1):
            weekday = date(year, month, day).strftime('%A')
            f.write(
                f'<strong>{weekday}, {this_month} {p.ordinal(day)}, {year}</strong><br><br><br>')
            f.write('<strong>END LOG</strong><br>')
            f.write('____________________________________________________________________________<br><br>')
        f.write('</p>')

make_logs(3, 2021)
