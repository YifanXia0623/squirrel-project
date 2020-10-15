from django.shortcuts import render

def index(Request):
    return render(request, 'adopt/index.html', {})

