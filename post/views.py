from django.shortcuts import render
from .models import Author, Entry

# Create your views here.

def queries(response):
    #  get all authors
    # authors = Author.objects.all()

    #  get first N elements [:N]
    # authors = Author.objects.all()[:10]

    #  get elements from X to N [0:5]
    authors = Author.objects.all()[0:5]

    # filter by field, this return an array
    fAuthors = Author.objects.filter(email='fostercarlos@example.net')

    # ge an element
    author = Author.objects.get(id=1)

    return render(response, 'post/queries.html', {
        'authors': authors, 
        'filteredAuths': fAuthors,
        'singleAuthor': author
    })