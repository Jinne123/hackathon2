from django.shortcuts import render
from .models import Tarief

# Create your views here.
def index(request):
    return render(request, "index.html")

def location(request):
    return render(request, "location.html")

def route(request):
    mapbox_access_token = 'pk.eyJ1Ijoib2xraWUiLCJhIjoiY2w4d293cnZ1MDZhNDNubXQ1NzJoZXZqcyJ9.Q7wuS_3ptDCLIryumOz3vA'
    starttarief = Tarief.objects.get(id=1).starttarief
    per_kilometer = Tarief.objects.get(id=1).per_kilometer
    afstand = 10
    afstand_kilometer = afstand * per_kilometer
    total = starttarief + (afstand * per_kilometer)
    return render(request, "route.html", { "starttarief": starttarief, "per_kilometer": per_kilometer, "afstand": afstand, "total": total, "afstand_kilometer": afstand_kilometer, "mapbox_access_token": mapbox_access_token })

def progress(request):
    mapbox_access_token = 'pk.eyJ1Ijoib2xraWUiLCJhIjoiY2w4d293cnZ1MDZhNDNubXQ1NzJoZXZqcyJ9.Q7wuS_3ptDCLIryumOz3vA'
    starttarief = Tarief.objects.get(id=1).starttarief
    per_kilometer = Tarief.objects.get(id=1).per_kilometer
    afstand = 10
    afstand_kilometer = afstand * per_kilometer
    total = starttarief + (afstand * per_kilometer)
    return render(request, "progress.html", { "starttarief": starttarief, "per_kilometer": per_kilometer, "afstand": afstand, "total": total, "afstand_kilometer": afstand_kilometer, "mapbox_access_token": mapbox_access_token })