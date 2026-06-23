from django.shortcuts import render

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