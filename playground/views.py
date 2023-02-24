from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def calculate():
    x = 1
    y = 2
    x += y
    return x


def say_hello(request):
    x = calculate()
    return render(request, 'Hello.html', {'name': 'Jacob'})
