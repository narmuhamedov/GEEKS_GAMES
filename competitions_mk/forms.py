from django import forms
from . import models

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = models.Participants
        fields = '__all__'
