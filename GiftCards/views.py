from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'home.html'


def homepage(request):
    # return HttpResponse('homepage')
    return render(request, 'homepage.html')


def about(request):
    # return HttpResponse('about')
    return render(request, 'about.html')
