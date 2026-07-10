from django.db import models
from mortal_kombat.models import PersonMk

class Participants(models.Model):
    name = models.CharField(max_length=50)
    choice_hero = models.ForeignKey(PersonMk, on_delete=models.CASCADE, verbose_name='fighter')
    personal_data = models.FileField(upload_to='competitions/')
    cash = models.PositiveIntegerField(default=1000)
    
    created_at = models.DateField(auto_now_add=True)

