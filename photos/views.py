from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
import datetime as dt

def welcome( request ):
    return HttpResponse ('welcome to my gallery')

def photos_of_day(request):
    date = dt.date.today()
    photos = Article.todays_photos()
    return render(request, 'all-photos/today-photos.html',{'date': date,"photos":photos})

def past_days_photos(request,past_date):
    
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(photos_today)
    
    photos = Article.days_photos(date)
    return render(request, 'all-photos/past-photos.html', {"date":date, 'photos':photos})
