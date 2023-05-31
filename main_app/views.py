from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Book

# Create your views here.
def home(request):
    # Include an .html file extension - unlike when rendering EJS templates
    return render(request, 'home.html')
def about(request):
    # Include an .html file extension - unlike when rendering EJS templates
    return render(request, 'about.html')
def books_index(request):
    books = Book.objects.all()
    # Include an .html file extension - unlike when rendering EJS templates
    return render(request, 'books/index.html', {
    'books': books
    })
def books_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'books/detail.html', {
        'book': book
    })

class BookCreate(CreateView):
    model = Book
    fields = '__all__'

class BookUpdate(UpdateView):
    model = Book
    fields = ['title', 'genre', 'published']

class BookDelete(DeleteView):
    model = Book
    success_url = '/books'