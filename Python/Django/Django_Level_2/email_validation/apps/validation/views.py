from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from .models import User
# Create your views here.
def index(req):
    return render(req, 'validation/index.html')
def validation(req):
    if req.method == 'POST':
        print req.POST['email']
        if User.userManager.validation(req.POST['email']):
            User.userManager.create(email = req.POST['email'])
            messages.info(req, "The email you entered ({}) is a valid email address! Thank you!".format(req.POST['email']))
            return redirect('/success')
        else:
            messages.info(req, "Email is not valid!")
            return redirect('/')
def success(req):
    context = {
        "emails": User.userManager.all()
    }
    print context
    return render(req, 'validation/success.html', context)
