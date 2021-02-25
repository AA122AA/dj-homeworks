from django.db.models.manager import BaseManager
from django.shortcuts import render
from phones.models import Phone
from django.http.request import HttpRequest


def sorting(sort:str):
    s_list = []
    if sort == "name":
        s_list = list(Phone.objects.order_by("name"))
    elif sort == "min_price":
        s_list = list(Phone.objects.order_by("-price"))
    elif sort == "max_price":
        s_list = list(Phone.objects.order_by("price"))
    else:
        s_list = Phone.objects.all()
    return s_list


def show_catalog(request:HttpRequest):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    if sort:
        s_list = sorting(sort)
        context = {"phones": list(s_list)}
    else:
        phones = Phone.objects.all()
        context = {"phones": list(phones)}
    
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    p = Phone.objects.filter(slug=slug).get()
    context = {"phone": p}
    return render(request, template, context)
