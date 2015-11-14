from django.db import models

# Create your models here.

class Author(models.Model):
    AuthorID = models.CharField(max_length=20,primary_key=True)
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
class Book(models.Model):
    title = models.CharField(max_length=30)
    AuthorID = models.ForeignKey(Author)
    isbn = models.CharField(max_length=20,primary_key=True)
    publisher =models.CharField(max_length=20)
    PublishDate =models.CharField(max_length=20)
    price = models.CharField(max_length=20)