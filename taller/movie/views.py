from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
# Create your views here.

def home(request):
    searchTerm = request.GET.get('searchMovie')
    movies = Movie.objects.all()
    if searchTerm:
        movies = movies.filter(title__icontains=searchTerm)
    return render(request, 'home.html', { 'searchTerm': searchTerm, 'movies': movies })

def about(request):
    return HttpResponse('<h1>Welcome to about page</h1>')