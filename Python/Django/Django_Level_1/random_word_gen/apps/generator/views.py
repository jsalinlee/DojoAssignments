from django.shortcuts import render, redirect
import random
import string
def index(request):
    if 'count' not in request.session:
        request.session['count'] = 1
    return render(request, 'generator/index.html')
def generate(request):
    request.session['count'] += 1
    request.session['random_word'] = ''
    for i in range(0, 16):
        request.session['random_word'] += (random.choice(string.ascii_uppercase + string.digits))
    return redirect("/")
