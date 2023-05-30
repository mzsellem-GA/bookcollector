from django.shortcuts import render

books = [
    {'title': 'The Body Keeps The Score', 'genre': 'self-help', 'published': 2010},
    {'title': 'Shadow and Bone', 'genre': 'fantasy', 'published': 2003},
]

# Create your views here.
def home(request):
    # Include an .html file extension - unlike when rendering EJS templates
    return render(request, 'home.html')
def about(request):
    # Include an .html file extension - unlike when rendering EJS templates
    return render(request, 'about.html')
def books_index(request):
    # Include an .html file extension - unlike when rendering EJS templates
    return render(request, 'books/index.html', {
    'books': books
    })