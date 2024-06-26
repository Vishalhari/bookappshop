
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect
from q import q

from .forms import AuthorForm,BookForm

from .models import Book,Author

# Create your views here.

def index(request):
    return render(request,'base.html')

def createBook(request):
    books = Book.objects.all()

    if request.method == 'POST':
        form = BookForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect('booklist')
    else:
        form = BookForm()
    return render(request,'admin/book.html',{'form':form})

def Listbook(request):
    books = Book.objects.all()

    paginator = Paginator(books,2)
    pagenumber = request.GET.get('page')

    try:
        page = paginator.get_page(pagenumber)
    except EmptyPage:
        page =  paginator.page(pagenumber.num_pages)

    return render(request, 'admin/listbook.html', {'books': books,'page':page})

def Bookdetails(request,book_id):
    book = Book.objects.get(id=book_id)

    return render(request,'admin/bookdetails.html',{'books':book})


def Listauthor(request):
    authors = Author.objects.all()
    return render(request,'admin/listauthor.html',{'authors':authors})

def CreateAuthor(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('listauthor')
    else:
        form = AuthorForm()
    return render(request, 'admin/createauthor.html', {'form': form})


def UpdateAuthor(request,author_id):
    author = Author.objects.get(id=author_id)

    if request.method == 'POST':
        form = AuthorForm(request.POST,instance=author)

        if form.is_valid():
            form.save()
            return redirect('listauthor')
    else:
        form = AuthorForm(instance=author)
    return render(request,'admin/updateauthor.html',{'form':form})



def UpdateBook(request,book_id):
    book = Book.objects.get(id=book_id)

    if request.method == 'POST':
        form = BookForm(request.POST,request.FILES,instance=book)

        if form.is_valid():
            form.save()

            return redirect('booklist')
    else:
        form = BookForm(instance=book)
    return render(request,'admin/updatebook.html',{'form':form})

def deleteauthor(request,author_id):
    author = Author.objects.get(id=author_id)

    if request.method == 'POST':
        author.delete()
        return redirect('listauthor')

    return render(request, 'admin/deleteauthor.html', {'author': author})


def deletebook(request,book_id):
    book = Book.objects.get(id=book_id)


    if request.method =='POST':
        book.delete()

        return redirect('booklist')

    return render(request,'admin/delete_book.html',{'book':book})


def Search_book(request):
    query = None
    books = None

    if 'q' in request.GET:
        query = request.GET.get('q')
        books = Book.objects.filter(Q(title__icontains=query))
    else:
        books = []

    context = {'books':books,'query':query}

    return render(request,'admin/search.html',context)


