from django.contrib import admin
from .import models
# Register your models here.

class Book_Category_Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('category_name',)}
    list_display = ['category_name', 'slug']


admin.site.register(models.Book_Category, Book_Category_Admin)