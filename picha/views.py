from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
from .models import *

# Create your views here.
def home(request):
    return HttpResponse('Our pictures goes here!')