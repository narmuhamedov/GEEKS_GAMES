from django.shortcuts import render, get_object_or_404
from . import models

#detail
def person_detail_view(request, id):
    if request.method == 'GET':
        person_id = get_object_or_404(models.PersonMk, id=id)
    return render(request, 'persons/person_detail.html', {'pers_id': person_id})



#list
def person_mk_view(request):
    if request.method == 'GET':
        persons = models.PersonMk.objects.all().order_by('-id')
        news = models.NewsMk.objects.all().order_by('-id')
    return render(request, 'persons/person_list.html', 
    {
        'pers': persons,
        'news': news
        
    })













def person_mk(request):
    if request.method == "GET":
        pers1 = {
            'title': "Jonny Cage",
            'hp': 100,
            'style': 'тхэквондо, карате',
            'arkana': 'green speed',
            'friends': ['Sonya', 'Jax', 'Scorpion', 'Kenshi']
        }
    return render(request, 'pers1.html', pers1)

def ninja_mk(request):
    if request.method == "GET":
        context = {
            'title': 'NINJA MK',
            'characters': [
                {
                    "name": "Hazjo Hasashi",
                    "nickname": "Scorpion",
                    "weapons" : ['kunai', 'katana']
                },

                {
                    'name': "Kuai Liang",
                    'nickname': "Sub-Zero",
                    'weapons': ['ice ball']
                },

                {
                    'name': "Bi Khan",
                    'nickname': "Noob Saibot",
                    'weapons': ['shadow man', 'серп']
                }

            ]
        }
    return render(request, 'ninja_mk.html', context)