from django.conf.urls import patterns, url

from jobs import views

urlpatterns = patterns('',
	url(r'^jobs/$', views.JobIndexView.as_view(), name='job_index'),
	url(r'^jobs/(?P<pk>\d+)/$', views.JobDetailView.as_view(), name='job_detail'),
	url(r'^jobs/(?P<pk>\d+)/edit/$', views.JobUpdate.as_view(), name='job_update'),
	url(r'^clients/$', views.ClientIndexView.as_view(), name='client_index'),
	url(r'^clients/(?P<pk>\d+)/$', views.ClientDetail.as_view(), name='client_detail'),
	url(r'^clients/(?P<pk>\d+)/edit/$', views.ClientUpdate.as_view(), name='client_update'),
	)