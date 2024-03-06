from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    paginator = Paginator(books, 2)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    context = {
        'books_list': page_obj,
    }
    return render(request, template, context)


def books_page(request, pub_date):
    template = 'books/books_list.html'
    books = Book.objects.filter(pub_date=pub_date)
    books_all = Book.objects.all()
    print(books_all)
    context = {
        'books_list': books,
        'books_all': books_all,
    }
    return render(request, template, context)
