from django.contrib import admin
from .models import Book_Details, BorrowModel
# Register your models here.

admin.site.register(Book_Details)
admin.site.register(BorrowModel)
