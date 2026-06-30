from django.urls import path
from . import views


urlpatterns = [
    path('hero_list/', views.game_list_view, name='hero'),
]