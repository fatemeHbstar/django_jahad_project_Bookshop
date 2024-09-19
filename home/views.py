from django.shortcuts import render
from books.models import *
# Create your views here.

context = {}
books = Book.objects.all()
context["books"] = books


def home(request):
    return render(request, "home/homepage.html", {"books": books, "authors": Author.objects.all()})


def bestselling(request):
    return render(request, "home/bestSellerspage.html", context)


def fiction(request):
    return render(request, "home/fictionBookspage.html", context)


def authors(request):
    authors = Author.objects.all()
    return render(request, "home/authors.html", {"authors": authors})


def studybooks(request):
    return render(request, "home/studyBookspage.html", context)
