from django.shortcuts import render, redirect, HttpResponse
import random, datetime

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['activity'] = ''
    return render(request, 'ninja_gold/index.html')
def process_money(request):
    if request.POST['building'] == 'farm':
        earn_gold = random.randint(10, 20)
        request.session['gold'] += earn_gold
        activity = "Earned {} gold from the {}!".format(earn_gold, request.POST['building'])
    if request.POST['building'] == 'cave':
        earn_gold = random.randint(5, 10)
        request.session['gold'] += earn_gold
        activity = "Earned {} gold from the {}!".format(earn_gold, request.POST['building'])
    if request.POST['building'] == 'house':
        earn_gold = random.randint(2, 5)
        request.session['gold'] += earn_gold
        activity = "Earned {} gold from the {}!".format(earn_gold, request.POST['building'])
    if request.POST['building'] == 'casino':
        earn_gold = random.randint(-50, 50)
        request.session['gold'] += earn_gold
        if earn_gold < 0:
            activity = "Lost {} gold from the {}!".format(abs(earn_gold), request.POST['building'])
            text_color = 'red'
        else:
            activity = "Earned {} gold from the {}!".format(earn_gold, request.POST['building'])
    request.session['activity'] += '\n' + activity + " " + datetime.datetime.now().strftime('%m/%d/%y %H:%M %p')
    text_color = 'green'
    return redirect('/')
