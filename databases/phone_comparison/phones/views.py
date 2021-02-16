from django.shortcuts import render

from phones.models import Phone, Apple, Samsung, Nokia


def show_catalog(request):
    template = 'catalog.html'
    phones = []
    phones.append(list(Apple.objects.all()))
    phones.append(list(Samsung.objects.all()))
    phones.append(list(Nokia.objects.all()))

    context = {"phones": phones}
    return render(request, template, context)
