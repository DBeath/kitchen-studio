from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.db import transaction

from jobs.models import Job, JobEvent, Client

# def index(request):
# 	jobs_list = Job.objects.all()
# 	context = {'jobs_list': jobs_list}
# 	return render(request, 'jobs/index.html', context)

# def detail(request, job_id):
# 	return HttpResponse("You're looking at job %s." % job_id)

def getObjectList(objects):
	objectList = list(objects)
	objectList.sort(key=getLCD)
	return objectList


class JobIndexView(generic.ListView):
	template_name = 'jobs/job_index.html'
	context_object_name = 'job_list'
	queryset = Job.objects.order_by('-consultation_date')


class JobDetailView(generic.DetailView):
	model = Job
	template_name = 'jobs/job_detail.html'


class ClientIndexView(generic.ListView):
	template_name = 'jobs/client_index.html'
	context_object_name = 'client_list'
	queryset = Client.objects.order_by('last_name')


class ClientDetailView(generic.DetailView):
	model = Client
	template_name = 'jobs/client_detail.html'
