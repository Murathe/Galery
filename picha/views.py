from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
from .models import *

# Create your views here.
def base(request):
    
    return render(request, 'common/navbar.html', {"date": date})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'common/search.html', {"message": message, "images": searched_images})
    else:
        message = "Make sure you've searched a term"
        return render(request, 'common/search.html', {"message": message})

def photo_category(request):
    date = dt.date.today()
    picha = Image.objects.all()

    return render(request, 'common/category.html', {"date": date, "picha": picha})