from django.shortcuts import render


#Create your views here.

#View basada en función:

def generos_view(request): 
    return render(request, 'generos/generos.html', {})


