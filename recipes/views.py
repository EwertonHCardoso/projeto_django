from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    print(home)
    return HttpResponse('home2')

def sobre(request):
    print('sobre')
    return HttpResponse('sobre')

