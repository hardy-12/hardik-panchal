from django.shortcuts import render
from django.http import HttpResponse

def homepageview(request):
    return HttpResponse("Welcome Pyapp to HomePage")


def aboutusview(request):
    return HttpResponse("Welcome Pyapp to About us")    


def contactview(request):
    return HttpResponse("Welcome Pyapp to Contact Us")    