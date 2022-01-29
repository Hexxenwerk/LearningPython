import calendar
import datetime

year: int = int(input("Gib das Jahr ein, z.B. 1998 oder 0 für das aktuelle Jahr: "))
month: int = int(input("Gib den Monat ein, z.B. 10 oder 0 für den aktuellen Monat: "))

if not year:
    year = datetime.date.today().year

if not month:
    month = datetime.date.today().month

for i in range(1, calendar.monthrange(year, month)[1]+1):
    print(f"{i}.{month:02}.{year}")
