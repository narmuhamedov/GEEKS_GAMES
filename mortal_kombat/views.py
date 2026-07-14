from django.shortcuts import render, get_object_or_404
from . import models
from django.db.models import F
from django.views import generic




#detail
class PersonDetailView(generic.DetailView):
    template_name = 'persons/person_detail.html'
    context_object_name = 'pers_id'
    pk_url_kwarg = 'id'
    model = models.PersonMk

    def get_object(self, queryset = None):
        obj = super().get_object(queryset)
        request = self.request
        views_blog = request.session.get('viewed_blog', [])

        if obj.pk not in views_blog:
            self.model.objects.filter(pk=obj.pk).update(views=F('views')+1)
            views_blog.append(obj.pk)
            request.session['viewed_blog'] = views_blog
            obj.refresh_from_db()
        return obj





# def person_detail_view(request, id):
#     if request.method == 'GET':
#         person_id = get_object_or_404(models.PersonMk, id=id)

#         views_blog = request.session.get('viewed_blog', [])

#         if id not in views_blog:
#             person_id.views = F("views")+1
#             person_id.save()
#             person_id.refresh_from_db()
#         views_blog.append(id)
#         request.session['viewed_blog'] = views_blog


#     return render(request, 'persons/person_detail.html', {'pers_id': person_id})



#list

class PersonsMkListView(generic.ListView):
    template_name = 'persons/person_list.html'
    model = models.PersonMk
    context_object_name = 'pers'
    ordering = ['-id']

    def get_queryset(self):
        return self.model.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = models.NewsMk.objects.all().order_by('-id')
        return context



# def person_mk_view(request):
#     if request.method == 'GET':
#         persons = models.PersonMk.objects.all().order_by('-id')
#         news = models.NewsMk.objects.all().order_by('-id')
#     return render(request, 'persons/person_list.html', 
#     {
#         'pers': persons,
#         'news': news
        
#     })















class PersonMkView(generic.TemplateView):
    template_name = 'pers1.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': "Jonny Cage",
            'hp': 100,
            'style': 'тхэквондо, карате',
            'arkana': 'green speed',
            'friends': ['Sonya', 'Jax', 'Scorpion', 'Kenshi']
        })
        return context


# def person_mk(request):
#     if request.method == "GET":
#         pers1 = {
#             'title': "Jonny Cage",
#             'hp': 100,
#             'style': 'тхэквондо, карате',
#             'arkana': 'green speed',
#             'friends': ['Sonya', 'Jax', 'Scorpion', 'Kenshi']
#         }
#     return render(request, 'pers1.html', pers1)




class NinjaMKView(generic.TemplateView):
    template_name = 'ninja_mk.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'NINJA MK'
        context['characters'] =  [
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
        return context




# def ninja_mk(request):
#     if request.method == "GET":
#         context = {
#             'title': 'NINJA MK',
#             'characters': [
#                 {
#                     "name": "Hazjo Hasashi",
#                     "nickname": "Scorpion",
#                     "weapons" : ['kunai', 'katana']
#                 },

#                 {
#                     'name': "Kuai Liang",
#                     'nickname': "Sub-Zero",
#                     'weapons': ['ice ball']
#                 },

#                 {
#                     'name': "Bi Khan",
#                     'nickname': "Noob Saibot",
#                     'weapons': ['shadow man', 'серп']
#                 }

#             ]
#         }
#     return render(request, 'ninja_mk.html', context)