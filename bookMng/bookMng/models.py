from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class MainMenu(models.Model):
    item = models.CharField(max_length=200, unique=True)
    link = models.CharField(max_length=500, unique=True)

    def __str__(self):
        return self.item


class Book(models.Model):
    name = models.CharField(max_length=200)
    web = models.URLField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    publishdate = models.DateField(auto_now=True)
    picture = models.FileField(upload_to='bookEx/static/uploads')
    pic_path = models.CharField(max_length=200, editable=False, blank=True)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    rating = models.DecimalField(decimal_places=2, max_digits=4, default=0)
    num_ratings = models.DecimalField(decimal_places=0, max_digits=8, default=0)

    def __str__(self):
        return str(self.id)


class Favorite(models.Model):
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    book_id = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)


class Comment(models.Model):
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    book_id = models.IntegerField(default=0)
    comment_id = id
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=800)

    def __str__(self):
        return str(self.id)


