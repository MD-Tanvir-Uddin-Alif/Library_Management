from django.shortcuts import render, redirect
from .forms import DepositeForm
from visitor.models import VisitorModel
from django.contrib.auth.decorators import login_required
from visitor.views import send_transaction_mail
# Create your views here.

@login_required
def DepositeView(request):
    if request.method == 'POST':
        form = DepositeForm(request.POST)
        if form.is_valid():
            deposite_amount = form.cleaned_data['amount']

            user = request.user
            transaction = form.save(commit=False)
            transaction.account = user.visitormodel
            transaction.save()

            user.visitormodel.balance += deposite_amount
            user.visitormodel.save()
            send_transaction_mail(user,deposite_amount,"Deposite Message",'deposite_mail.html')

            return redirect('Profile_page')
    else:
        form = DepositeForm()
    
    return render(request,'registration_and_login_form.html',{'form': form, 'type': "Deposite"})





