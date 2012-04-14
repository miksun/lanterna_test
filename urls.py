from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'e_learning.views.index'),
    (r'^save/$', 'e_learning.views.save'),
	(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}),
	(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'accounts/logged_out.html'}),
    (r'^admin/', include(admin.site.urls)),
)
