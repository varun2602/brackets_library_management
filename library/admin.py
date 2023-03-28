from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.books)
class booksAdmin(admin.ModelAdmin):
    list_display = ['id', 'book_name', 'book_author', 'is_issued', 'issued_to']
