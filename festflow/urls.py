from django.conf.urls import include, url
from django.contrib.auth.views import logout
from . import views

urlpatterns = [
    # Home Page
    url(r'^$', views.index, name='index'),

    # social login urls
    url('', include('social.apps.django_app.urls', namespace='social')),

    # logout url
    url(r'^logout/$', logout,
        {'next_page': '/'})
]
