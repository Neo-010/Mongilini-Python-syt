from django.http import HttpResponse # type: ignore
from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from django.urls import reverse # type: ignore
from .forms import FilmForm
from film.models import Film
import logging


logger = logging.getLogger(__name__)

def list(request):
    films = Film.objects.all() 
    return render(request, 'film/film_list.html', {'films': films})

def home(request):
    films = Film.objects.all() 
    return render(request, 'home.html', {'films': films})

def create(request):
    if request.method == 'POST':
        form = FilmForm(request.POST, request.FILES)  # Обробка файлів
        if form.is_valid():
            film = form.save()
            logger.debug(f"Film created: {film.name}, Poster: {film.poster.url if film.poster else 'No poster uploaded'}")
            return redirect('home')
        else:
            logger.error(f"Form is invalid: {form.errors}")
    else:
        form = FilmForm()
    return render(request, 'film/create.html', {'form': form})

def details(request, id):
    film = Film.objects.get(id=id)

    return render(request, "details.html", {"film": film})



def view_film(request, pk):
    film = get_object_or_404(Film, pk=pk)
    return render(request, 'view_film.html', {'film': film})

def edit(request, pk):
    # Отримуємо фільм за pk
    film = get_object_or_404(Film, pk=pk)

    # Якщо форма була надіслана (POST)
    if request.method == 'POST':
        form = FilmForm(request.POST, request.FILES, instance=film)  # Передаємо існуючий об'єкт для редагування
        if form.is_valid():
            film = form.save()  # Зберігаємо зміни
            logger.debug(f"Film updated: {film.name}, Poster: {film.poster.url if film.poster else 'No poster uploaded'}")
            return redirect('list')  # Перенаправлення на домашню сторінку
        else:
            logger.error(f"Form is invalid: {form.errors}")
    else:
        form = FilmForm(instance=film)  # Заповнюємо форму існуючими даними

    return render(request, 'edit.html', {'form': form, 'film': film})


def about(request):
    return HttpResponse("<h1>About Page!</h1>")

def layout_view(request):
    return render(request, '_layout.html')

def delete(request, pk):
    film = get_object_or_404(Film, pk=pk)
    if request.method == "POST":
        film.delete()
        return redirect('list')  # редірект на сторінку списку фільмів
    return render(request, 'delete_film.html', {'film': film})


def toggle_favorite(request, pk):
    film = get_object_or_404(Film, pk=pk)
    film.is_favorite = not film.is_favorite  # Перемикаємо статус "улюблений"
    film.save()
    
    # Перенаправляємо на сторінку зі списком улюблених фільмів
    return redirect('favorite_list')  # Перенаправлення на список улюблених фільмів

def favorite_list(request):
    films = Film.objects.filter(is_favorite=True)  # Отримуємо тільки улюблені фільми
    return render(request, 'favorite.html', {'films': films}) 

