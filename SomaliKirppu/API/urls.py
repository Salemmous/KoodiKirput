from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^suggest/(?P<word>.+)', views.suggest, name='suggest'),
    url(r'^translation/(?P<word>.+)', views.translation, name='translation'),
    url(r'^id/(?P<id>.+)', views.id, name='id'),
    url(r'^edit/(?P<id>.+)/(?P<en>.+)/(?P<so>.+)', views.edit, name='edit'),
    url(r'^edit', views.edit, name='edit'),
]