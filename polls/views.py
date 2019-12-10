from django.views import generic

from .models import Company, Worker, Job
from .forms import CreateJobForm, HireWorkerForm, AddWorkTimeForm

class CompaniesView(generic.ListView):
    template_name='polls/companies.html'
    queryset = Company.objects.order_by('company_name')

class CompanyDetailsView(generic.DetailView):
    template_name = 'polls/company_details.html'
    model = Company

class WorkersView(generic.ListView):
    template_name = 'polls/workers.html'
    queryset = Worker.objects.order_by('name')
    context_object_name = 'workers_list'

class WorkerDetailsView(generic.DetailView):
    template_name = 'polls/worker_details.html'
    model = Worker

class CreateJobView(generic.CreateView):
    template_name = 'polls/create_job.html'
    form_class = CreateJobForm
    success_url = '/' 

class HireWorkerView(generic.edit.FormView):
    template_name = 'polls/hire_worker.html'
    form_class = HireWorkerForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class AddWorkTimeView(generic.edit.FormView):
    template_name = 'polls/add_worktime.html'
    form_class = AddWorkTimeForm
    success_url = '/'

    def form_valid(self, form):
        form.add()
        return super().form_valid(form)