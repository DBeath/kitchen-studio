from django.conf.urls import patterns, url

from jobs import views

urlpatterns = patterns('',
	url(r'^jobs/$', views.JobIndexView.as_view(), name='job_index'),
	url(r'^jobs/(?P<pk>\d+)/$', views.JobDetailView.as_view(), name='job_detail'),
	url(r'^clients/$', views.ClientIndexView.as_view(), name='client_index'),
	url(r'^clients/(?P<pk>\d+)/$', views.ClientDetailView.as_view(), name='client_detail')
	)