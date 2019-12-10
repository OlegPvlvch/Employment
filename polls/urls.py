from django.urls import path

from . import views

urlpatterns = [
    path('', views.CompaniesView.as_view(), name='index'),
    path('<int:pk>', views.CompanyDetailsView.as_view(), name='get_details'),
    path('workers', views.WorkersView.as_view(), name='workers'),
    path('workers/<int:pk>', views.WorkerDetailsView.as_view(), name='worker_details'),
    path('create_job/', views.CreateJobView.as_view(), name='create_job'),
    path('hire/', views.HireWorkerView.as_view(), name='create_workplace'),
    path('addworktime/', views.AddWorkTimeView.as_view(), name='addworktime')
]
