from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from .models import Company

def index(request):
    companys_list = Company.objects.order_by('company_name')
    return render(request, 'polls/index.html', context = {'companys_list' : companys_list})

def get_details(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    return render(request, 'polls/details.html', context = {'company' : company})
