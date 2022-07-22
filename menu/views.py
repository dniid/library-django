from django.shortcuts import render


def menuView(request):
    return render(request, 'index.html')
