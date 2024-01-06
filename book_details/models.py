from django.db import models
from book_category.models import Book_Category
from visitor.models import VisitorModel
# Create your models here.

class Book_Details(models.Model):
    image = models.ImageField(upload_to='book_details/media/uploads/', blank = True, null = True)
    book_name = models.CharField(max_length = 30)
    book_descriptions = models.TextField()
    book_price = models.CharField(max_length = 40)
    book_category = models.ForeignKey(Book_Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.book_name
    

class Comment(models.Model):
    post = models.ForeignKey(Book_Details, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comments by {self.name}"
    

class BorrowModel(models.Model):
    book = models.ForeignKey(Book_Details, on_delete=models.CASCADE)
    user = models.ForeignKey(VisitorModel, on_delete=models.CASCADE)
    time_stamp = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=30,default="Nothing")
    borrow_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}-{self.book.book_name}"