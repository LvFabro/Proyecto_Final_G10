from django.shortcuts import render

#Create your views here.

def generos_view(request):
    return render(request, 'generos.html', {})