import calendar

def get_weekends(year):
    months = {1: 'JANEIRO', 2: 'FEVEREIRO', 3: 'MARÇO', 4: 'ABRIL', 5: 'MAIO', 
              6: 'JUNHO', 7: 'JULHO', 8: 'AGOSTO', 9: 'SETEMBRO', 10: 'OUTUBRO',
              11: 'NOVEMBRO', 12: 'DEZEMBRO'}
    
    weekends = {}
    
    for month in range(1, 13):
        weekends[months[month]] = []
        month_calendar = calendar.monthcalendar(year, month)
        
        for week in month_calendar:
            if week[calendar.SATURDAY] != 0:
                weekends[months[month]].append(f"sab {week[calendar.SATURDAY]}")
            if week[calendar.SUNDAY] != 0:
                weekends[months[month]].append(f"dom {week[calendar.SUNDAY]}")
    
    return weekends

weekends_2025 = get_weekends(2025)
weekends_2025
