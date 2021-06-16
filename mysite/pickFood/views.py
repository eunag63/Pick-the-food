from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Food

def index(request):
    foods = Food.objects.all()

    return render(request, 'pickFood/index.html')
