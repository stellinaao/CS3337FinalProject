from django.contrib import admin

# Register your models here.

from .models import MainMenu
from .models import Book
from .models import Favorite
from .models import Comment


admin.site.register(MainMenu)
admin.site.register(Book)
admin.site.register(Favorite)
admin.site.register(Comment)
