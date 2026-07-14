from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.views import generic

#search

class SearchView(generic.ListView):
    template_name = 'crud/read.html'
    context_object_name = 'part'
    model = models.Participants

    def get_queryset(self):
        return self.model.objects.filter(name__icontains=self.request.GET.get('s'))
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = self.request.GET.get('s')
        return context
    






# def search_view(request):
#     query = request.GET.get('s', '')
#     if query:
#         participant = models.Participants.objects.filter(name__icontains=query)
#         if not participant.exists():
#             return HttpResponse('Человек не найден')
#     else:
#         return HttpResponse('Человек не найден')

#     return render(request, 'crud/read.html', {'part': participant})





#create

class CreateParticipantView(generic.CreateView):
    template_name = 'crud/create.html'
    form_class = forms.ParticipantForm
    model = models.Participants
    success_url = '/participants_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateParticipantView, self).form_valid(form=form)


# def create_participant_view(request):
#     if request.method == 'POST':
#         form = forms.ParticipantForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('/participants_list/')
#     else:
#         form = forms.ParticipantForm()
#     return render(request, 'crud/create.html', {'form': form})

#read
class ParticipantListView(generic.ListView):
    template_name = 'crud/read.html'
    model = models.Participants
    paginate_by = 2
    ordering = ['-id']

    def get_queryset(self):
        return self.model.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['part'] = context['page_obj']
        return context



# def participant_list_view(request):
#     if request.method == "GET":
#         participant = models.Participants.objects.all().order_by('-id')
#         paginator = Paginator(participant, 2)
#         page = request.GET.get('page')
#         page_obj = paginator.get_page(page)

#     return render(request, 'crud/read.html', {'part': page_obj})

#update
class UpdateParticipantView(generic.UpdateView):
    template_name = 'crud/update.html'
    form_class = forms.ParticipantForm
    success_url = '/participants_list/'
    model = models.Participants

    def get_object(self, **kwargs):
        part_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=part_id)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateParticipantView, self).form_valid(form=form)
    
        





# def update_participant_view(request, id):
#     part_id = get_object_or_404(models.Participants, id=id)
#     if request.method == "POST":
#         form = forms.ParticipantForm(request.POST, instance=part_id)
#         if form.is_valid():
#             form.save()
#             return redirect('/participants_list/')
#     else:
#         form = forms.ParticipantForm(instance=part_id)
#     return render(request, 'crud/update.html', {'form': form, 'part_id': part_id})


#delete
class DeleteParticipantView(generic.DeleteView):
    template_name = 'crud/conf_del.html'
    success_url = '/participants_list/'
    context_object_name = 'part_id'
    model = models.Participants

    def get_object(self, **kwargs):
        part_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=part_id)
    



# def delete_participant_view(request, id):
#     part_id = get_object_or_404(models.Participants, id=id)
#     part_id.delete()
#     return redirect('/participants_list/')