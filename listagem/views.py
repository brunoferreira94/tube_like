from django.shortcuts import render
from django.views.generic import ListView, TemplateView, View
from  .models import Video

class listagem(ListView):
    model = Video
    template_name = 'listagem/home.html'