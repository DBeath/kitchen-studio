from django.db import models
import datetime
from django.utils import timezone
from django.db.models import Max
import operator

JOB_STATUS_CHOICES = (
		('cl', 'Consultation'),
		('pr', 'Priced'),
		('sl', 'Sold'),
		('ds', 'Designed'),
		('ws', 'Work Started'),
		('wf', 'Work Finished'),
	)

STREET_TYPE_CHOICES = (
		('st', 'Street'),
		('rd', 'Road'),
		('av', 'Avenue'),
		('cs', 'Crescent'),
		('bv', 'Boulevard'),
	)

PHONE_TYPE_CHOICES = (
		('hm', 'Home'),
		('wk', 'Work'),
		('fx', 'Fax'),
		('mb', 'Mobile'),
	)

class Address(models.Model):
	number = models.CharField(max_length=10)
	street = models.CharField(max_length=50)
	street_type = models.CharField(max_length=2, choices=STREET_TYPE_CHOICES)
	suburb = models.CharField(max_length=30,blank=True, null=True)
	city = models.CharField(max_length=30)

	def __unicode__(self):
		address_string = u"%s %s %s" % (self.number, self.street, 
			self.get_street_type_display())
		return address_string

class Client(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField(blank=True, null=True)
	address = models.ManyToManyField(Address, through='ClientAddress', blank=True, null=True)

	def __unicode__(self):
		return u"%s %s" % (self.first_name, self.last_name)

class ClientAddress(models.Model):
	client = models.ForeignKey(Client)
	address = models.ForeignKey(Address)
	date_added = models.DateField(auto_now_add=True)

class Phone(models.Model):
	client = models.ForeignKey(Client)
	area_code = models.CharField(max_length=10, blank=True, null=True)
	number = models.CharField(max_length=30)
	phone_type = models.CharField(max_length=2, choices=PHONE_TYPE_CHOICES)

	def __unicode__(self):
		phone_string = u"%s : (%s) %s" % (self.get_phone_type_display(), 
			self.area_code, self.number)
		return phone_string


class Job(models.Model):
	client = models.ForeignKey(Client)
	address = models.ForeignKey(Address)
	budget = models.IntegerField(blank=True, null=True)
	estimated_cost = models.IntegerField(blank=True, null=True)

	def __unicode__(self):
		job_string = u"%s | %s" % (self.client, self.address)
		return job_string

	def latest_consultation_date(self):
		return self.jobevent_set.filter(job_status__contains='cl').latest('date').date

	def latest_event(self):
		return self.jobevent_set.latest('date')
		

class JobEvent(models.Model):
	job_status = models.CharField(max_length=2, choices=JOB_STATUS_CHOICES)
	date = models.DateField()
	job = models.ForeignKey(Job)
	comment = models.TextField(blank=True, null=True)

	def __unicode__(self):
		jobevent_string = u"%s on %s" % (self.get_job_status_display(), self.date)
		return jobevent_string

		
# def getLCD(job):
# 	return job.latest_consultation_date()

# jobs.sort(key=getLCD)

