from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request, 'una_health_app/index.html')

