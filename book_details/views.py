from django.shortcuts import render, redirect
from .models import Book_Details, BorrowModel
from .import forms
from visitor.models import VisitorModel
from django.views.generic import DeleteView
# Create your views here.

class detailiView(DeleteView):
    model = Book_Details
    pk_url_kwarg = 'id'
    template_name = 'book_detail.html'

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object # post model er object ekhane store korlam
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
    

def borrow_view(request, id):
    if request.method == 'POST':
        book = Book_Details.objects.get(id=id)
        user = request.user.visitormodel
        if user.balance >= int(book.book_price):
            user.balance -= int(book.book_price)
            user.save()
            borrow = BorrowModel.objects.create(book=book,user=user,borrow_status=True,title="Borrowed")
            # print(borrow.borrow_status)
            borrow.save()

        return redirect('Profile_page')
    
    return render(request,'profile.html',{'borrow':borrow})

def return_view(request, id):
    if request.method == 'POST':
        book = Book_Details.objects.get(id=id)
        user = request.user.visitormodel
        user.balance += int(book.book_price)
        user.save()
        borrow = BorrowModel.objects.create(book=book,user=user,borrow_status=False,title="Returned")
        borrow.save()

        return redirect('Profile_page')
    
    return render(request,'profile.html',{'borrow':borrow})
