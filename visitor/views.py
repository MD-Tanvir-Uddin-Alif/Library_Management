from django.shortcuts import render,redirect
from .forms import VisitorRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from book_details.models import Book_Details
from book_category.models import Book_Category
from book_details.models import BorrowModel
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
# Create your views here.

def send_transaction_mail(user, amount, subject, template):

    message = render_to_string(template,{
        'user' : user,
        'amount' : amount,
    })

    send_email = EmailMultiAlternatives(subject, '', to=[user.email])
    send_email.attach_alternative(message,"text/html")
    send_email.send()

def HomeView(request, category_slug = None):
    data = Book_Details.objects.all()
    if category_slug is not None:
        category = Book_Category.objects.get(slug = category_slug)
        data = Book_Details.objects.filter(book_category = category)
    categories = Book_Category.objects.all()
    return render(request,'home_page.html',{'data':data, 'category':categories})

def Registrationview(request):
    if request.method == 'POST':
        register_form = VisitorRegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,"Account Created Successfully")
            return redirect('Profile_page')
    else:
        register_form = VisitorRegistrationForm(request.POST)

    return render(request,'registration_and_login_form.html',{'form':register_form, 'type': 'Registration'})


@login_required
def user_profieView(request):
    user = request.user.visitormodel
    data = BorrowModel.objects.filter(user=user)
    return render(request,'profile.html',{'data':data})

def LoginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name, password=user_pass)
            if user is not None:
                messages.success(request, "Logged in to account Successfully")
                login(request, user)
                return redirect('Profile_page')
            else:
                messages.warning(request, "At first create an account")
                return redirect('Registration_page')
    else:
        form = AuthenticationForm()
        
    return render(request, 'registration_and_login_form.html', {'form': form, 'type': 'Login'})

    

def LogoutView(request):
    logout(request)
    return redirect('Login_page')
