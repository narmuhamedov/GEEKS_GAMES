from django.urls import path
from . import views

urlpatterns = [
    path('create_tournament/', views.CreateParticipantView.as_view(), name='create'),
    path('participants_list/', views.ParticipantListView.as_view(), name='read'),
    path('participants_list/<int:id>/update/', views.UpdateParticipantView.as_view(), name='update'),   
    path('participants_list/<int:id>/delete/', views.DeleteParticipantView.as_view(), name='delete'),
    path('search/', views.SearchView.as_view(), name='search'),   
]