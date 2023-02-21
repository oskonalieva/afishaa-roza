"""afishaa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from movie_app import views
from movie_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/test/', views.test_api),
    path('api/v1/movies/', movie_list_api_movies_view),
    path('api/v1/directors/', movie_list_api_directors_view),
    path('api/v1/reviews/', movie_list_api_reviews_view),
    path('api/v1/movies/<int:id>/', movie_detail_api_view),
    path('api/v1/directors/<int:id>/', directors_detail_api_view),
    path('api/v1/reviews/<int:id>/', review_detail_api_view),




]
