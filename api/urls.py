from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views


urlpatterns = [
    url(r'^teams/?$', views.teams),
    url(r'^matches/?$', views.matches),
    url(r'^players/?$', views.players),
]

urlpatterns = format_suffix_patterns(urlpatterns)