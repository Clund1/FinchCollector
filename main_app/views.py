from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from . models import Finch


# VIEWS
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()

    return render(request, 'finches/index.html', {
        'finches': finches
    })

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)

    return render(request, 'finches/detail.html', { 
        'finch': finch 
    })

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'