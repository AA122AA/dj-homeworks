from django.db.models.manager import BaseManager
from django.shortcuts import render
from phones.models import Phone
from django.http.request import HttpRequest


def sorting(sort:str, phones:BaseManager):
    s_list = []
    if sort == "name":
        s_list = sorted(
            list(phones), 
            key=lambda phone: phone.name
            )
    elif sort == "min_price":
        s_list = sorted(
            list(phones), 
            key=lambda phone: phone.price,
            reverse=True
            )
    elif sort == "max_price":
       s_list = sorted(
            list(phones), 
            key=lambda phone: phone.price,
            reverse=False
            )
    else:
        s_list = phones
    return s_list


def show_catalog(request:HttpRequest):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    phones = Phone.objects.all()
    context = {"phones": list(phones)}
    if sort:
        s_list = sorting(sort, phones)
        context = {"phones": list(s_list)}
    
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    p = Phone.objects.filter(slug=slug).get()
    context = {"phone": p}
    return render(request, template, context)
