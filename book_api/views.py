from django.shortcuts import render
from book_api.models import Book
from django.http import JsonResponse

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    booksPython = list(books.values())
    return JsonResponse({
        'books': booksPython
    })
    
    