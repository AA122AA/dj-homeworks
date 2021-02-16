from django.shortcuts import render
from django.core.paginator import Paginator

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
    paginator = Paginator(dates(books), 10)
    page = paginator.get_page(page_number)
    next_page_url = reverse(bus_stations) + "?" + urlencode({"page":str(page_number + 1)})
    prev_page_url = reverse(bus_stations) + "?" + urlencode({"page":str(page_number - 1)})
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
