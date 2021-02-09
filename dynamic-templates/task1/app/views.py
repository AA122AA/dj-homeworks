from django.shortcuts import render

import csv

def createList()->list:
    dataList = []
    with open("inflation_russia.csv", "r") as f:
        reader = csv.DictReader(f, delimiter = ";")    
        for row in reader:
            val = list(row.values())
            for v in range(len(val)):
                if val[v] == "":
                    val[v] = "0"
            print(list(row.values()))
            # Убрать это и переделать на мердж словарей нормальный с проверкой на пустые строки
            data = {}
            data["Year"] = row.get("Год")
            data["Jan"] = float(row.get("Янв", "-"))
            data["Feb"] = float(row.get("Фев", "-"))
            data["Mar"] = float(row.get("Мар", "-"))
            data["Apr"] = float(row.get("Апр", "-"))
            data["May"] = float(row.get("Май", "-"))
            data["Jun"] = float(row.get("Июн", "-"))
            data["Jul"] = float(row.get("Июл", "-"))
            data["Aug"] = float(row.get("Авг", "-"))
            data["Sep"] = float(row.get("Сен", "-"))
            data["Oct"] = float(row.get("Окт", "-"))
            data["Now"] = float(row.get("Ноя", "-"))
            data["Dec"] = float(row.get("Дек", "-"))
            data["Sum"] = float(row.get("Суммарная", "-"))
            dataList.append(data)
    return dataList
 

def inflation_view(request):
    template_name = 'inflation.html'
    print(*createList(), sep="\n")

       # чтение csv-файла и заполнение контекста
    context = {
        "data": createList(), 
        "headers": list(createList()[0].keys())
        }

    return render(request, template_name,
                  context)