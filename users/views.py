from django.shortcuts import render,HttpResponse
from .forms import RegisterForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        username=form.cleaned_data.get('username')
        messages.success(request,f'welcome{username} your account is created')
        return HttpResponse("success")

    else:
        form=RegisterForm()
    return render(request,'users/register.html',{'form':form})

