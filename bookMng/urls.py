from django.urls import path
from . import views

from bookMng.views import Register

urlpatterns = [
    path('', views.index, name='index'),
    path('postbook', views.postbook, name='postbook'),
    path('displaybooks', views.displaybooks, name='displaybooks'),
    path('book_detail/<int:book_id>', views.book_detail, name='book_detail'),
    path('mybooks', views.mybooks, name='mybooks'),
    path('book_delete/<int:book_id>', views.book_delete, name='book_delete'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('book_detail/book_detail_rate/<int:book_id>', views.book_detail_rate, name='book_detail_rate'),
    path('book_detail_rate/<int:book_id>', views.book_detail_rate, name='book_detail_rate'),
    path('myfavorites', views.myfavorites, name='myfavorites'),
    path('book_add_favorite/<int:book_id>', views.book_add_favorite, name='book_add_favorite'),
    path('book_delete_favorite/<int:book_id>', views.book_delete_favorite, name='book_delete_favorite'),
    path('book_search', views.book_search, name='book_search'),
    path('book_detail/book_search', views.book_search, name='book_search'),
    path('search', views.search, name='search'),
    path('book_detail/add_comment/<int:book_id>', views.add_comment, name='add_comment'),
    path('add_comment/<int:book_id>', views.add_comment, name='add_comment'),
    path('delete_comment/<int:comment_id>', views.delete_comment, name='delete_comment'),
    # path('search_results', views.search_results, name='search_results'),
]


