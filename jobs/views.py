from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.db import transaction

from jobs.models import Job, JobEvent

# def index(request):
# 	jobs_list = Job.objects.all()
# 	context = {'jobs_list': jobs_list}
# 	return render(request, 'jobs/index.html', context)

# def detail(request, job_id):
# 	return HttpResponse("You're looking at job %s." % job_id)

def getLCD(job):
	return str(job.latest_consultation_date())


def getObjectList(objects):
	objectList = list(objects)
	objectList.sort(key=getLCD)
	return objectList


class IndexView(generic.ListView):
	template_name = 'jobs/index.html'
	context_object_name = 'jobs_list'
	#queryset = Job.objects.all()
	queryset = getObjectList(Job.objects.all())
	

class DetailView(generic.DetailView):
	model = Job
	template_name = 'jobs/detail.html'
