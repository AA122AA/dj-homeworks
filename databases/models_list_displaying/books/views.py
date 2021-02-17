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
    books = Book.objects.all()
    context = {"books": books}
    pub_dates = dates(books)
    print(pub_dates)
    #отсортировать даты, затем добавлять элемент до и элемент после в сраницу
    next_page_url = reverse("books") + "/" + date
    prev_page_url = reverse("books") + "/" + date
    if date:
        try:
            books = []
            books_data = Book.objects.filter(pub_date=str(date.date()))
            for book in books_data:
                books.append(book)
            if books:
                context = {"books": books}
        except Book.DoesNotExist:
            pass

    return render(request, template, context)
