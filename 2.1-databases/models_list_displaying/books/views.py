from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {'books': books}
    return render(request, template, context)

# def book_pub_date(request, pub_date):
#     template = 'books/books_list.html'
#     books = Book.objects.filter(pub_date=pub_date)
#     context = {'books': books}
#     return render(request, template, context)

def view_page(request, pub_date=None):
    template = 'books/books_list.html'
    books = Book.objects.filter(pub_date=pub_date)
    paginator = Paginator(books, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(pub_date)
    for i in page_obj.paginator:
        print(i)
    context = {
        'books': books,
        'page_obj': page_obj,
        }

    return render(request, template, context)