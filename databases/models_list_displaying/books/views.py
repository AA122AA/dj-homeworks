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
       
    #отсортировать даты, затем добавлять элемент до и элемент после в сраницу
    if date:
        pub_dates = sorted(list(set(dates(books))))
        index_date = 0
        for d in pub_dates:
            if d == date:
                index_date = pub_dates.index(d)
                break
        next_page_url = ""
        try:
            next_page_url = pub_dates[index_date+1]
        except IndexError:
            pass
        prev_page_url = pub_dates[index_date-1]
        try:
            books = []
            books_data = Book.objects.filter(pub_date=str(date))
            for book in books_data:
                books.append(book)
            if books:
                context = {
                    "books": books,
                    "next": next_page_url,
                    "prev": prev_page_url,
                    }
        except Book.DoesNotExist:
            pass

    return render(request, template, context)
