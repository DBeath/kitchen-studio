from django.contrib import admin
from jobs.models import Client, Job, Address, JobEvent, ClientAddress, Phone

class ClientAddressInline(admin.TabularInline):
	model = Client.address.through
	extra = 1

class PhoneAdmin(admin.TabularInline):
	model = Phone
	extra = 1

class JobInline(admin.TabularInline):
	model = Job
	extra = 0

class ClientAdmin(admin.ModelAdmin):
	fieldsets = [
		('Name', {'fields': ['first_name', 'last_name']}),
		('Email', {'fields': ['email']})
	]
	list_display = ('__unicode__', 'email')
	ordering = ('last_name',)
	inlines = [ClientAddressInline, PhoneAdmin, JobInline]

class AddressAdmin(admin.ModelAdmin):
	inlines = [ClientAddressInline]

class EventInline(admin.TabularInline):
	model = JobEvent
	extra = 1

class JobAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', 'latest_consultation_date', 'latest_event')
	inlines = [EventInline]


		

admin.site.register(Address, AddressAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Job, JobAdmin)