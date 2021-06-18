from django.urls import path
from . import views
import pickFood.views

urlpatterns = [
    path('', views.index),
    path('click/', pickFood.views.pick, name='pick')
]
