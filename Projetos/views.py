from django.shortcuts import render

def home(request):
    return render(request, 'Projetos/index.html')