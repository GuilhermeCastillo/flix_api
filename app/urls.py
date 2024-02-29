"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateListView, GenreRetrieveUpdateDestroyView
from actors.views import ActorCreateListView, ActorRetrieveUpdateDestroyView
from movies.views import MovieCreateListView, MovieRetrieveUpdateDestroyView
from reviews.views import ReviewCreateListView, ReviewRetrieveUpdateDestroyView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("genres/", GenreCreateListView.as_view(), name="genre"),
    path(
        "genres/<int:pk>/",
        GenreRetrieveUpdateDestroyView.as_view(),
        name="genre-detail-view",
    ),
    path("actors/", ActorCreateListView.as_view(), name="actor-create-list"),
    path(
        "actors/<int:pk>/",
        ActorRetrieveUpdateDestroyView.as_view,
        name="actor-detail-view",
    ),
    path("movies/", MovieCreateListView.as_view(), name="movie-create-list"),
    path(
        "movies/<int:pk>/",
        MovieRetrieveUpdateDestroyView.as_view(),
        name="movie-detail-view",
    ),
    path("reviews/", ReviewCreateListView.as_view(), name="review-create-list"),
    path(
        "reviews/<int:pk>/",
        ReviewRetrieveUpdateDestroyView.as_view(),
        name="review-detail-view",
    ),
]
