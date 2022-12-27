from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def projects(request):
    return render(request, 'main/projects.html')

def resume(request):
    return render(request, 'main/resume.html')

def contact(request):
    return render(request, 'main/contact.html')

def tanks(request):
    return render(request, 'main/tanks.html')

def canvas(request):
    return render(request, 'main/canvastesting.html')