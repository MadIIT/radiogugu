from django.shortcuts import render

def first(request):
    return render(request, 'first.html')


def start(request):
    return render(request, 'start_.html')
