from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Food, Post

from django.db.models import Max
import random

from hitcount.views import HitCountDetailView

def index(request):
    return render(request, 'pickFood/index.html')

def get_random():
    max_id = Food.objects.all().aggregate(max_id=Max("id"))['max_id']
    while True:
        pk = random.randint(1, max_id)
        food =     Food.objects.filter(pk=pk).first()
        if food:
            return food

def pick(request):
    food = get_random()
    return render(request, 'pickFood/click.html', {'food':food})

def click(request):
    return render(request, 'pickFood/click.html', context)

class PostDetail(HitCountDetailView):
    model = Post
    template_name = 'pickFood/click.html'
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context.update({
            'popular_posts': Post.objects.order_by('-hit_count_generic__hits')[:3],
        })
        return context
