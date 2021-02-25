from django.shortcuts import render
from django.core.paginator import Paginator
from django.urls import reverse

from urllib.parse import urlencode
from books.models import Book
from datetime import datetime


def dates(books):
    dates = []
    for book in books:
        dates.append(book.pub_date)
    return dates

    

def books_view(request, date:datetime=None):
    template = 'books/books_list.html'
    if date:
        sorted_books = Book.objects.order_by("pub_date")
        books = list(sorted_books.filter(pub_date = str(date)))
        next_page_url = Book.objects.filter(pub_date__gt=str(date)).order_by('pub_date').first()
        if next_page_url == None:
            next_page_url = sorted_books.first()
        prev_page_url = Book.objects.filter(pub_date__lt=str(date)).order_by('-pub_date').first()
        if prev_page_url == None:
            prev_page_url = sorted_books.last()
        context = {
            "books": books,
            "next": next_page_url.pub_date,
            "prev": prev_page_url.pub_date,
        }
    else:
        books = Book.objects.all()
        context = {"books": books}
    #отсортировать даты, затем добавлять элемент до и элемент после в сраницу
    return render(request, template, context)
