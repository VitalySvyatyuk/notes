from django.conf.urls import url, include

from . import views
  
urlpatterns = [
    url(r'^mynotes', views.mynotes, name='mynotes'),
    url(r'^$', views.index, name='index'),
    
]