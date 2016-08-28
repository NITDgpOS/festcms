from django.conf.urls import include, url
from django.contrib.auth.views import logout
from . import views

urlpatterns = [
    # Home Page
    url(r'^$', views.index, name='index'),

    # Event View Page
    url(r'^events/(?P<event_identifier>[a-z]*)/$', views.event_view,
        name='event_view'),

    # social login urls
    url('', include('social.apps.django_app.urls', namespace='social')),

    # Form to complete profile
    url(r'^complete_profile/$', views.complete_profile,
        name='complete_profile'),

    # logout url
    url(r'^logout/$', logout,
        {'next_page': '/'})
]
