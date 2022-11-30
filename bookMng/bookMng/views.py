from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from .models import MainMenu, Favorite, Book, Comment

from .forms import BookForm, BookRating, BookComment

from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


def index(request):
    return render(request, 'bookMng/index.html',
                  {
                      'item_list': MainMenu.objects.all()
                  })


def postbook(request):
    submitted = False
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            book = form.save(commit=False)
            try:
                book.username = request.user
            except Exception:
                pass
            book.save()
            return HttpResponseRedirect('/postbook?submitted=True')
    else:
        form = BookForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request,
                  'bookMng/postbook.html',
                  {
                      'form': form,
                      'item_list': MainMenu.objects.all(),
                      'submitted': submitted
                  })


def displaybooks(request):
    books = Book.objects.all()
    for b in books:
        b.pic_path = b.picture.url[14:]
    return render(request,
                  'bookMng/displaybooks.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books
                  })


def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    book.pic_path = book.picture.url[14:]
    return render(request,
                  'bookMng/book_detail.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'comments': Comment.objects.filter(book_id=book_id),
                      'user_comments': Comment.objects.filter(book_id=book_id, username=request.user),
                      'book': book
                  })


class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)


def mybooks(request):
    print("in")
    books = Book.objects.filter(username=request.user)
    print("in")
    for b in books:
        b.pic_path = b.picture.url[14:]
        print("done")
    return render(request,
                  'bookMng/mybooks.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books
                  })


def book_delete(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return render(request,
                  'bookMng/book_delete.html',
                  {
                      'item_list': MainMenu.objects.all(),
                  })


def aboutus(request):
    return render(request,
                  "bookMng/aboutus.html",
                  {
                      "item_list": MainMenu.objects.all()
                  })


def book_detail_rate(request, book_id):
    book = Book.objects.get(id=book_id)

    if request.method == 'POST':
        form = BookRating(request.POST, instance=book)
        curr_rating = book.rating
        if form.is_valid():
            book = form.save(commit=False)
            print("outside try")
            try:
                print("inside try")
                book.num_ratings += 1
                print("num_ratings: " + str(book.num_ratings))
                new_rating = book.rating

                book.rating = (curr_rating + new_rating) / book.num_ratings
                print("done")

            except Exception:
                print(str(Exception))
                pass
            book.save()
            return HttpResponseRedirect('../book_detail/' + str(book_id))
    else:
        form = BookRating()

    return render(request,
                  'bookMng/book_detail_rate.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'book': book,
                      'form': form,
                  })


def myfavorites(request):
    favorite_books = Favorite.objects.filter(username=request.user)
    books = []
    for fav_item in favorite_books:
        books += Book.objects.filter(id=fav_item.book_id)

    for b in books:
        b.pic_path = b.picture.url[14:]
    return render(request,
                  'bookMng/myfavorites.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books
                  })


def book_add_favorite(request, book_id):
    # book = Book.objects.get(id=book_id)
    inDB = False
    print("before for")

    for entry in Favorite.objects.all():
        print("in for")
        if (entry.username == request.user and entry.book_id == book_id):
            print("in if (not expected to print)")
            inDB = True
    print("outside for")

    print("outside if else")

    if inDB:
        pass

    else:
        print("Inside else")
        entry = Favorite.objects.create()
        print("outside try")
        try:
            entry.username = request.user
            entry.book_id = int(book_id)
        except Exception:
            pass
        entry.save()

    return HttpResponseRedirect('/displaybooks')

def book_delete_favorite(request, book_id):
    print("Inside View")
    favorite_book = Favorite.objects.filter(username=request.user, book_id=book_id)
    print("After get book")
    # book = Book.objects.get(id=)
    # for fav_item in favorite_books:
    #     books += Book.objects.filter(id=fav_item.book_id)

    # book = Book.objects.get(id=book_id)
    favorite_book.delete()
    print("done deleting")
    return render(request,
                  'bookMng/book_delete_favorite.html',
                  {
                      'item_list': MainMenu.objects.all(),
                  })


def book_search(request):
    book_input = request.POST.get('book_input')
    print(book_input)
    books_name = []
    # books_author = []
    try:
        books_name = list(Book.objects.filter(name=book_input))
    except Exception:
        print("exception in names")
        books_name = []
        pass

    # books_author = list(Book.objects.filter(username=book_input))

    # try:
    #     books_author = list(Book.objects.get(username=book_input))
    # except Exception:
    #     print("exception in authors")
    #     books_author = []
    #     pass

    # books = books_name + books_author

    return render(request,
                  'bookMng/book_search.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books_name,
                  })

def search(request):
    if request.method == 'POST':
        book_input = request.POST.get('book_input')
        print(book_input)
        books_name = []
        try:
            books_name = list(Book.objects.filter(name=book_input))
        except Exception:
            print("exception in names")
            books_name = []
            pass
        return render(request,
                      'bookMng/book_search.html',
                      {
                          'item_list': MainMenu.objects.all(),
                          'books': books_name,
                      })

    else:
        return render(request,
                      'bookMng/search.html',
                      {
                          'item_list': MainMenu.objects.all(),
                      })

def add_comment(request, book_id):
    book = Book.objects.get(id=book_id)

    if request.method == 'POST':
        form = BookComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            try:
                comment.username = request.user
                comment.book_id = book_id
            except Exception:
                pass
            comment.save()
            return HttpResponseRedirect('../book_detail/' + str(book_id))
    else:
        form = BookComment()

    # only returns if the access to view is not after a form submission (i.e., the first page access)
    return render(request,
                  'bookMng/add_comment.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'book': book,
                      'form': form,
                  })

def delete_comment(request, comment_id):
    comment = Comment.objects.filter(username=request.user, id=comment_id)
    comment.delete()
    print("done deleting")
    return render(request,
                  'bookMng/delete_comment.html',
                  {
                      'item_list': MainMenu.objects.all(),
                  })

