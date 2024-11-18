from django.http import HttpResponse
from django.shortcuts import render

def displayHomepage(request):
    return render(request, "home_page.html")
