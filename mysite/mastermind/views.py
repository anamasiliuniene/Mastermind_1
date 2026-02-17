from django.http import HttpResponse


def home(request):
    return HttpResponse("Mastermind veikia 🚀")


from django.shortcuts import render

# Create your views here.
