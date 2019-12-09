from django import forms
from .models import Job, Worker, WorkPlace

class CreateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields=['name', 'company']
        labels={
            'company' : 'Company',
            'name':'Description'
        }

class HireWorkerForm(forms.Form):
    job = forms.ModelChoiceField(
                queryset=Job.objects.all())
    worker = forms.ModelChoiceField(
                queryset=Worker.objects.all())
    
    def save(self):
        WorkPlace.objects.create(
            job = self.cleaned_data['job'],
            worker = self.cleaned_data['worker']
        )
