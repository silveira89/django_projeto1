from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.htm')


def contato(request):
    return render(request, 'contato.htm')


def sobre(request):
    return render(request, 'sobre.htm')
