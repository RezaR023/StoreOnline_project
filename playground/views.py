from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def say_hello(request):
    return render(request, 'hello.html', {'name': 'Reza'})


def tem_func(request):
    x = 1
    y = 2
    return render(request, 'temp2.html')
