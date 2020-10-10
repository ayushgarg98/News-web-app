from django.urls import path

from . import views

app_name = "news"

urlpatterns = [
    path('', views.index, name = 'index'),
    path('international/', views.international, name = 'international'),
    path('sports/', views.sports, name = 'sports'),
    path('business/', views.business, name = 'business'),
    path('technology/', views.technology, name = 'technology'),
    path('search/<str:q>', views.search, name = 'search'),
]