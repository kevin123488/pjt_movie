from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('up_to/', views.up_to, name='up_to'),
    path('stars/', views.stars, name='stars'),
    path('db/', views.db, name='db'),
    path('detail/<int:movie_pk>/', views.detail, name='detail'),
    path('like/<int:movie_pk>/', views.movie_like, name='movie_like'),
]
