from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    paginator = Paginator(books, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'books_list': page_obj,
        }
    return render(request, template, context)


def view_page(request, pub_date=None):
    template = 'books/books_list.html'
    books = Book.objects.filter(pub_date=pub_date)
    books_all = Book.objects.all()
    context = {
        'books_list': books,
        'books_all': books_all,
        }

    return render(request, template, context)