from django.shortcuts import render
from django.http import HttpResponse
# Create your views here
from .models import Vilege


def index(request):
    vilege = Vilege.objects.all()
    return render(request, 'vilege/index.html', { 'vilege': vilege })
