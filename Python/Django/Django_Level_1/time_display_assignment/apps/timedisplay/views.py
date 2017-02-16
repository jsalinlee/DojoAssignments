from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    context = {
        "datetime" : datetime.datetime.now()
    }
    return render(request, 'timedisplay/index.html', context)
