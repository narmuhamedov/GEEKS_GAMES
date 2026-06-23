from django.urls import path
from . import views

urlpatterns = [
    path('first_person/', views.person_mk, name='jony_cage'),
    path('ninja/', views.ninja_mk, name='ninja'),
]