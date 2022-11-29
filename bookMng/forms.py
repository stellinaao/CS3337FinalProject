from django import forms
from django.forms import ModelForm
from .models import Book, Comment


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'name',
            'web',
            'price',
            'picture',
        ]


class BookRating(ModelForm):
    class Meta:
        model = Book
        fields = [
            'rating',
        ]


# class Search(ModelForm):
#     class Meta:
#         model = Book
#         fields = [
#             'name',
#         ]

class BookComment(ModelForm):
    class Meta:
        model = Comment
        fields = [
            'title',
            'body',
        ]