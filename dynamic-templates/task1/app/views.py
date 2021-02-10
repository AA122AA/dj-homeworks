from django.shortcuts import render

import csv

def createList()->list:
    dataList = []
    with open("inflation_russia.csv", "r") as f:
        reader = csv.DictReader(f, delimiter = ";")    
        for row in reader:
            dataList.append(row)
    return dataList
 

def inflation_view(request):
    template_name = 'inflation.html'
    context = {
        "data": createList(), 
        "headers": list(createList()[0].keys())
        }

    return render(request, template_name,
                  context)