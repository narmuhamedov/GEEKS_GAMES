from django.urls import path
from . import views

urlpatterns = [
    path('first_person/', views.PersonMkView.as_view(), name='jony_cage'),
    path('', views.NinjaMKView.as_view(), name='ninja'),
    path('person_list/', views.PersonsMkListView.as_view(), name='mk_list'),
    path('person_list/<int:id>/', views.PersonDetailView.as_view(), name='person_detail'),
]