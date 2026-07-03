from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms

#create
def create_participant_view(request):
    if request.method == 'POST':
        form = forms.ParticipantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/participants_list/')
    else:
        form = forms.ParticipantForm()
    return render(request, 'crud/create.html', {'form': form})

#read
def participant_list_view(request):
    if request.method == "GET":
        participant = models.Participants.objects.all().order_by('-id')
    return render(request, 'crud/read.html', {'part': participant})

#update
def update_participant_view(request, id):
    part_id = get_object_or_404(models.Participants, id=id)
    if request.method == "POST":
        form = forms.ParticipantForm(request.POST, instance=part_id)
        if form.is_valid():
            form.save()
            return redirect('/participants_list/')
    else:
        form = forms.ParticipantForm(instance=part_id)
    return render(request, 'crud/update.html', {'form': form, 'part_id': part_id})


#delete
def delete_participant_view(request, id):
    part_id = get_object_or_404(models.Participants, id=id)
    part_id.delete()
    return redirect('/participants_list/')