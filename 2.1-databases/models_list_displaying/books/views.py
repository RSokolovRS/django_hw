from django.core.paginator import Paginator
from django.shortcuts import render
from books.converters import DateConverter
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
    books_all = Book.objects.filter(pub_date=pub_date)
    pub_date_list = sorted(Book.objects.values_list('pub_date', flat=True))

    def view_pud_date(n, m):
        for i in n:
            for index, pub_date in enumerate(m):
                if m[index] == i.pub_date and index == len(m) - 1:
                    date = [m[index - 1], m[0]]
                    return date
                elif m[index] == i.pub_date:
                    date = [m[index - 1], m[index + 1]]
                    return date

    context = {
        'books_list': books_all,
        'books_all': view_pud_date(books_all, pub_date_list),
    }
    return render(request, template, context)
