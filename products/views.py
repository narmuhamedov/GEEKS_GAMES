from django.shortcuts import render
from . import models

def game_list_view(request):
    if request.method == 'GET':
        heros = models.Hero.objects.all()
        persons = models.Person.objects.all()
        context = {
            'heros': heros,
            'person': persons
        }
    return render(request, template_name='heros.html', context=context)
