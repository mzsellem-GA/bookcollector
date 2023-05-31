from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Book
from .forms import ChapterForm

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
    chapter_form = ChapterForm()
    return render(request, 'books/detail.html', {
        'book': book, 'chapter_form': chapter_form
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

def add_chapter(request, book_id):
 # create a ModelForm instance using the data in request.POST
  form = ChapterForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_chapter = form.save(commit=False)
    new_chapter.book_id = book_id
    new_chapter.save()
  return redirect('detail', book_id=book_id)
