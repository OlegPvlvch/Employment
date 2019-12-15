from django import forms
from .models import Job, Worker, WorkPlace, WorkTime
import datetime

class CreateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields=['name', 'company']
        labels={
            'company' : 'Company',
            'name' : 'Description'
        }

class HireWorkerForm(forms.Form):
    job = forms.ModelChoiceField(
                queryset=Job.objects.all())
    worker = forms.ModelChoiceField(
                queryset=Worker.objects.all())
    
    def save(self):
        if self.cleaned_data['worker'].workplace_set.all():
            last_place = self.cleaned_data['worker'].workplace_set.order_by('-id')[0]
            last_place.status = 'Cancelled'
            last_place.save()
        WorkPlace.objects.create(
            job = self.cleaned_data['job'],
            worker = self.cleaned_data['worker']
        )

class AddWorkTimeForm(forms.Form):
    worker = forms.ModelChoiceField(
                queryset=Worker.objects.all())
    work_place = forms.ModelChoiceField(
                queryset=WorkPlace.objects.filter(worktime__isnull=True))
    date_start = forms.DateTimeField()
    date_end = forms.DateTimeField(initial=datetime.date.today)

    def add(self):
        WorkTime.objects.create(
            date_start = self.cleaned_data.get('date_start'),
            date_end = self.cleaned_data.get('date_end'),
            worker = self.cleaned_data.get('worker'),
            workplace = self.cleaned_data.get('work_place')
        )
        