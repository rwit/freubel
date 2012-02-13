from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout

admin.autodiscover()

urlpatterns = patterns('',
#    url(r'^polls/$', 'polls.views.index'),
#    url(r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),
#    url(r'^polls/(?P<poll_id>\d+)/results/$', 'polls.views.results'),
#    url(r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
    url(r'^bencotto', login),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/logout/$', logout),
    url(r'^accounts/profile/$', 'accounts.views.profile')
)
admin.autodiscover()