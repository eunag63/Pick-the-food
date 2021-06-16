from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Food

def index(request):
    foods = Food.objects.all()
    str = ''
    for food in foods:
        str += "<p>{}<br>".format(food.name)
        str += food.introduction+"</p>"
    return HttpResponse(str)
