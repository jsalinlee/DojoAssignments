from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'disappearing_ninjas/index.html')
def ninjas(request):
    if ninjas:
        turtle = "disappearing_ninjas/img/tmnt.png"
    context = {
    'turtle': turtle
    }
    return render(request, 'disappearing_ninjas/ninjas.html', context)
def ninjas_color(request, color):
    if color == "blue":
        turtle = "disappearing_ninjas/img/leonardo.jpg"
    elif color == "orange":
        turtle = "disappearing_ninjas/img/michelangelo.jpg"
    elif color == "red":
        turtle = "disappearing_ninjas/img/raphael.jpg"
    elif color == "purple":
        turtle = "disappearing_ninjas/img/donatello.jpg"
    else:
        turtle = "disappearing_ninjas/img/notapril.jpg"

    context = {
        'turtle': turtle
    }
    return render(request, 'disappearing_ninjas/ninjas.html', context)
