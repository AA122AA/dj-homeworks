from django import template
from datetime import datetime
import time


register = template.Library()


@register.filter
def format_date(value:float):
    time_delta = time.time()-value
    if time_delta < 600:
        return "Только что"
    elif time_delta < 3600:
        return f"{datetime.fromtimestamp(time_delta).strftime('%M')} минут назад"
    elif time.time() - value < 86400:
        return f"{datetime.fromtimestamp(time_delta).strftime('%H')} часов назад"
    else:
        return f"{datetime.fromtimestamp(value).strftime('%y-%m-%d')}"


@register.filter
def format_score(value, arg):
    if value < -5:
        return "Все плохо"
    elif -5 < value < 5:
        return "Нейтрально"
    elif value > 5:
        return "Хорошо"
    else:
        return arg


@register.filter
def format_num_comments(value, arg):
    if value == 0:
        return "Оставьте комментарий"
    elif 1 < value < 50:
        return value
    elif value > 50:
        return "50+"
    else:
         return arg


@register.filter
def format_selftext(value:str, arg):
    if value != "":
        l_value = value.split(" ")
        return " ".join(l_value[:arg]) + " ... " + " ".join(l_value[-5:])
    else: 
        return "Смотри обсуждение"

