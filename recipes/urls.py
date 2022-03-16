from django.urls import path, include
from . import views

app_name = 'recipes'
urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/<int:id>/', views.recipe, name='recipe'),
]