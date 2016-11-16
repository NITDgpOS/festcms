from django.conf.urls import include, url
from django.contrib.auth.views import logout
from . import views

urlpatterns = [
    # Home Page
    url(r'^$', views.index, name='index'),

    # About Page
    url(r'^about/$', views.about, name='about'),

    # Sponsors Page
    url(r'^sponsors/$', views.sponsors, name='sponsors'),

    # Contact Page
    url(r'^contact/$', views.contact, name='contact'),

    # Event Page
    url(r'^events/$', views.events, name='events'),

    # Reach Us Page
    url(r'^reachus/$', views.reachus, name='reachus'),

    # Event View Page
    url(r'^events/(?P<event_identifier>[a-z]*)/$', views.event_view,
        name='event_view'),

    # Event Register Page
    url(r'^register_event/(?P<event_identifier>[a-z]*)/$',
        views.register_event, name='register_event'),

    # Login Page
    url(r'^login/$',
        views.login_page, name='login_page'),


    # social login urls
    url('', include('social.apps.django_app.urls', namespace='social')),

    # Form to complete profile
    url(r'^complete_profile/$', views.complete_profile,
        name='complete_profile'),

    # logout url
    url(r'^logout/$', logout,
        {'next_page': '/'})
]
