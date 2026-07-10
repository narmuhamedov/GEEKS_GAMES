from django.urls import path
from . import views

urlpatterns = [
    path('first_person/', views.person_mk, name='jony_cage'),
    path('', views.ninja_mk, name='ninja'),
    path('person_list/', views.person_mk_view, name='mk_list'),
    path('person_list/<int:id>/', views.person_detail_view, name='person_detail'),
]