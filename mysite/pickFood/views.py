from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Food

def index(request):
    foods = Food.objects.all()
    context = {'foods':foods}
    return render(request, 'pickFood/index.html', context)

def click(request):
    return render(request, 'pickFood/click.html')
