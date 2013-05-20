from django.db import models
import datetime
from django.utils import timezone
from django.db.models import Max, Sum
import operator


class Address(models.Model):
	STREET = 'ST'
	ROAD = 'RD'
	AVENUE = 'AV'
	CRESCENT = 'CR'
	BOULEVARD = 'BL'
	STREET_TYPE_CHOICES = (
		(STREET, 'Street'),
		(ROAD, 'Road'),
		(AVENUE, 'Avenue'),
		(CRESCENT, 'Crescent'),
		(BOULEVARD, 'Boulevard'),
	)
	number = models.CharField(max_length=10)
	street = models.CharField(max_length=50)
	street_type = models.CharField(max_length=2, choices=STREET_TYPE_CHOICES)
	suburb = models.CharField(max_length=30,blank=True)
	city = models.CharField(max_length=30)

	def __unicode__(self):
		if (self.suburb != ""):
			address_string = u"%s %s %s, %s, %s" % (self.number, self.street, 
				self.get_street_type_display(), self.suburb, self.city)
		else:
			address_string = u"%s %s %s, %s" % (self.number, self.street,
				self.get_street_type_display(), self.city)
		return address_string

class Client(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField(blank=True, null=True)
	address = models.ManyToManyField(Address, through='ClientAddress', blank=True, 
		null=True)

	def __unicode__(self):
		return u"%s %s" % (self.first_name, self.last_name)

	def current_address(self):
		return self.clientaddress_set.latest('date_added').address

class ClientAddress(models.Model):
	client = models.ForeignKey(Client)
	address = models.ForeignKey(Address)
	date_added = models.DateField(auto_now_add=True)

class Phone(models.Model):
	HOME = 'HM'
	WORK = 'WK'
	FAX = 'FX'
	MOBILE = 'MB'
	PHONE_TYPE_CHOICES = (
		(HOME, 'Home'),
		(WORK, 'Work'),
		(FAX, 'Fax'),
		(MOBILE, 'Mobile'),
	)
	client = models.ForeignKey(Client)
	area_code = models.CharField(max_length=3, blank=True)
	number = models.CharField(max_length=15)
	phone_type = models.CharField(max_length=2, choices=PHONE_TYPE_CHOICES)

	def __unicode__(self):
		phone_string = u"%s : (%s) %s" % (self.get_phone_type_display(), 
			self.area_code, self.number)
		return phone_string


class Job(models.Model):
	client = models.ForeignKey(Client)
	address = models.ForeignKey(Address)
	budget = models.DecimalField(blank=True, null=True, max_digits=8, 
		decimal_places=2)
	final_price = models.DecimalField(blank=True, null=True, max_digits=8, 
		decimal_places=2)
	consultation_date = models.DateField()

	def __unicode__(self):
		job_string = u"%s | %s | Consultation on %s" % (self.client, self.address, 
			self.consultation_date)
		return job_string

	def latest_event(self):
		return self.jobevent_set.latest('date')

	def get_final_price(self):
		self.final_price = self.jobevent_set.aggregate(
			total_price=Sum('price'))['total_price']
		return self.final_price
		

class JobEvent(models.Model):
	CONSULTATION = 'CL'
	PRICED = 'PR'
	PENDING = 'PD'
	UNSOLD = 'US'
	SOLD = 'SD'
	ADDITIONAL_SALE = 'AS'
	DESIGNED = 'DS'
	INSTALL_DATE = 'ID'
	INSTALL_START = 'IS'
	INSTALL_FIN = 'IF'
	JOB_STATUS_CHOICES = (
		(CONSULTATION, 'Consultation'),
		(PRICED, 'Priced'),
		(PENDING, 'Pending'),
		(UNSOLD, 'Unsold'),
		(SOLD, 'Sold'),
		(ADDITIONAL_SALE, 'Additional Sale'),
		(DESIGNED, 'Designed'),
		(INSTALL_DATE, 'Installation Date'),
		(INSTALL_START, 'Installation Started'),
		(INSTALL_FIN, 'Installation Finished'),
	)	
	job_status = models.CharField(max_length=2, choices=JOB_STATUS_CHOICES)
	job = models.ForeignKey(Job)
	date = models.DateField()
	price = models.DecimalField(max_digits=8, decimal_places=2,
		help_text="Change in price.", blank=True, null=True)
	comment = models.TextField(blank=True, null=True)

	def __unicode__(self):
		jobevent_string = u"%s on %s" % (self.get_job_status_display(), self.date)
		return jobevent_string

# class SaleEvent(models.Model):
# 	job = models.ForeignKey(Job)
# 	price = models.DecimalField(max_digits=6, decimal_places=2)
# 	date = models.DateField()
# 	comment = models.TextField(blank=True, null=True)
		
# def getLCD(job):
# 	return job.latest_consultation_date()

# jobs.sort(key=getLCD)

