from django.shortcuts import render
from book_api.models import Book
from rest_framework.response import Response
from rest_framework.decorators import api_view
from book_api.serializer import BookSerializer

# Create your views here.
@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
    
    
    