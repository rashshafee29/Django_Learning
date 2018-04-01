from django.shortcuts import render


def index(request):
    return render(request, 'personal/home.html')


def contact(request):
    return render(request, 'personal/basic.html', {'content': ['if u will like to contact me mail me', 'rashidodd@gmail.com']})
