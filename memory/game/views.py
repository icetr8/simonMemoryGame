from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from raspicode import code

def index(request):
        return HttpResponse("Hello, world. You're at the polls index.")