import locale
import calendar

locale.setlocale(locale.LC_TIME, 'es_ES')

def mes_nombre(mes_numero):
    return calendar.month_name[mes_numero]


