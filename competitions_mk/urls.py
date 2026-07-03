from django.urls import path
from . import views

urlpatterns = [
    path('create_tournament/', views.create_participant_view, name='create'),
    path('participants_list/', views.participant_list_view, name='read'),
    path('participants_list/<int:id>/update/', views.update_participant_view, name='update'),   
    path('participants_list/<int:id>/delete/', views.delete_participant_view, name='delete'),   
]