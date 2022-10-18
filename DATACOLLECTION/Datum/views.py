from django.shortcuts import render


from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "Datum/welcome.html")


def welcome(request):
    return render(request, "Datum/datum.html")

    
def blog(request):
    return render(request, "Datum/congrats.html")


