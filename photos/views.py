from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime as dt

def welcome( request ):
    return HttpResponse ('welcome to my gallery')

def photos_of_day(request):
    date = dt.date.today()
    photos = Article.todays_photos()
    return render(request, 'all-photos/today-photos.html',{'date': date,"photos":photos})

