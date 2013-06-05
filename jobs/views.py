from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import UpdateView, CreateView, DeleteView

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from jobs.models import Job, JobEvent, Client
from jobs.forms import * #ClientUpdateForm, ClientFormSet

# def index(request):
#   jobs_list = Job.objects.all()
#   context = {'jobs_list': jobs_list}
#   return render(request, 'jobs/index.html', context)

# def detail(request, job_id):
#   return HttpResponse("You're looking at job %s." % job_id)

def getObjectList(objects):
    objectList = list(objects)
    objectList.sort(key=getLCD)
    return objectList


class JobIndexView(ListView):
    template_name = 'jobs/job_index.html'
    context_object_name = 'job_list'
    queryset = Job.objects.order_by('-consultation_date')


class JobDetailView(DetailView):
    model = Job
    template_name = 'jobs/job_detail.html'


class ClientIndexView(ListView):
    template_name = 'jobs/client_index.html'
    context_object_name = 'client_list'
    queryset = Client.objects.order_by('last_name')

class ClientCreateView(CreateView):
    model = Client

class ClientDetail(DetailView):
    model = Client
    template_name = 'jobs/client_detail.html'


class ClientUpdate(UpdateView):
    model = Client
    form_class = ClientUpdateForm

class JobUpdate(UpdateView):
    model = Job
    form_class = JobFormSet
        