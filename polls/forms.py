from django import forms
from .models import Job

class CreateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields=['name', 'company']
        labels={
            'company' : 'Company',
            'name':'Description'
        }