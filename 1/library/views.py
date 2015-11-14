import datetime 
import MySQLdb
# Create your views here.
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render_to_response
from library.models import Book,Author
from django.views.decorators.csrf import csrf_exempt
#def hello(request):
#    return HttpResponse("Hello World")
#def time1(request):
#    now = datetime.datetime.now()
#    return HttpResponse(now)
#def time3(request):
#    now =datetime.datetime.now()
#    c=Context({'time':now})
#   return render_to_response("time2.html",c)
@csrf_exempt
def add_book(request):
    authorlist = Author.objects.all()
    if request.POST:
        post = request.POST
        v = request.POST.get('AuthorID')
        a = Author.objects.get(AuthorID = v)
        book = Book(
            title = post["title"],
            AuthorID = a,
            isbn = post["isbn"],
            publisher = post["publisher"],
            PublishDate = post["PublishDate"],
            price = post["price"]
        )
        book.save()
    return render_to_response("add_book.html",locals())
def add_author(request):
    if request.POST:
        post = request.POST
        author = Author(
            AuthorID=post["AuthorID"],
            name = post["name"],
            age = post["age"],
            country = post ["country"]
        )
        author.save()
        #c={'book':new_book,'author':new_author}
    return render_to_response("add_author.html",locals())
def book_list(request):
    if request.method == "GET":
        if 'delete' in request.GET:
            t = request.GET['delete']
            s = Book.objects.filter(isbn = t)
            if s:
                Books = Book.objects.get(isbn = t)
                Books.delete()
        books = Book.objects.all()
        return render_to_response("book_list.html",{'books':books})
@csrf_exempt
def update(request,i):
    books = Book.objects.get(isbn = i)
    #authors = Author.objects.get(AuthorID = books.AuthorID.AuthorID)
    if request.method == "POST":
        books.title = request.POST["title"]
       #books.AuthorID = request.POST["AuthorID"]
       #isbn = post["isbn"],\
        books.publisher = request.POST["publisher"]
        books.PublishDate = request.POST["PublishDate"]
        books.price = request.POST["price"]
        books.save()
       # authors.AuthorID = request.POST["AuthorID"]
       # authors.name = request.POST["name"]
       # authors.age = request.POST["age"]
       # authors.country = request.POST["country"]
       # authors.save()
    books = Book.objects.get(isbn = i)
   # authors = Author.objects.get(AuthorID = books.AuthorID)
   # c={'books':books,'authors':authors}
    return render_to_response("update.html",locals())
def show(request,i):
    book = Book.objects.get(isbn = i)
    return render_to_response("show.html",locals()) 
def begin(request):
    return render_to_response("begin.html",)
def search(request):
    if request.POST:
        try:
            author= Author.objects.filter(name=request.POST["Author"])
            books = author[0].book_set.all()
            c = Context({"book":books})
            return render_to_response("show_book.html",c)
        except:
            return render_to_response("wrong_answer.html")       
def back_search(request):
    return render_to_response("search.html",)
