from django.shortcuts import render

# Create your views here.


def main(request, name):
    return render(request, 'djangoapp/home.html', {'name': name})