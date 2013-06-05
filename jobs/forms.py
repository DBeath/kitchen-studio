from django.forms.models import modelformset_factory, inlineformset_factory
from django.forms.formsets import formset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
import floppyforms as forms
from jobs.models import Client, Job, JobEvent


class JobUpdateForm(forms.ModelForm):
	class Meta:
		model = Job


	def __init__(self, *args, **kwargs):
		super(JobUpdateForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Submit'))


class JobEventForm(forms.ModelForm):
	class Meta:
		model = JobEvent


class ClientUpdateForm(forms.ModelForm):
	class Meta:
		exclude = ('address')
		model = Client

	def __init__(self, *args, **kwargs):
		super(ClientUpdateForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Submit'))
			
ClientFormSet = formset_factory(ClientUpdateForm, can_delete=True)
client_formset = ClientFormSet()

JobFormSet = inlineformset_factory(Job, JobEvent)
